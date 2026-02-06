from sqlalchemy import select
from typing import Optional, List
import bcrypt
from database.database import session_factory
from database.models.person import PersonOrm
from schemas.person import PersonLoginSchema, PersonSchema

class PersonService:
    @classmethod
    async def get_all(cls) -> List[PersonOrm]:
        stmt = select(PersonOrm)
        async with session_factory() as session:
            res = await session.execute(stmt)
            persons = res.scalars().all()

            return persons



    @classmethod
    async def get(cls, id: int, session: Optional[AsyncSession] = None) -> Optional[PersonOrm]:
        stmt = select(PersonOrm).where(PersonOrm.id == id)
        if session:
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        else:
            async with session_factory() as new_session:
                result = await new_session.execute(stmt)
                return result.scalar_one_or_none()
        


    @classmethod
    async def add(cls, person_data: PersonLoginSchema) -> PersonOrm:
        stmt = select(PersonOrm).where(PersonOrm.name == person_data.name)
        
    
        async with session_factory() as session:
            existing_person = await session.execute(stmt)

            if existing_person.scalar_one_or_none():
                raise ValueError(f"Пользователь с именем '{person_data.name}' уже существует")
            
            hashed_password = bcrypt.hashpw(
                person_data.password.encode('utf-8'),
                bcrypt.gensalt(rounds=12)
            ).decode('utf-8')

            person = PersonOrm(name=person_data.name, hashpassword=hashed_password)

            session.add(person)
            await session.commit()
            await session.refresh(person)
            return person


    @classmethod
    async def delete(cls, id: int) -> bool:

        async with session_factory() as session:
            person = await cls.get(id, session=session)
            
            if not person:
                return False
            
            await session.delete(person)
            await session.commit()
            return True
    
    @classmethod 
    async def update(cls, id: int, new_data: PersonSchema):
        async with session_factory() as session:
            person_to_update = await cls.get(id)
            if person_to_update:
                update_data = new_data.dict(exclude_unset=True)

                for key, value in update_data.items():
                    if hasattr(person_to_update, key):
                        setattr(person_to_update, key, value)
                session.add(person_to_update)
                await session.commit()
                await session.refresh(person_to_update)
        
                return person_to_update
            print('Пользователь не найден!')






    @classmethod
    async def verify_password(cls, person_data: PersonLoginSchema) -> bool:
        person = await cls.get(person_data.name)
        if not person:
            return False
        
        try:

            is_valid = bcrypt.checkpw(
                person_data.password.encode('utf-8'),
                person.hashpassword.encode('utf-8')
            )
            return is_valid
            
        except Exception as e:
            print(f"Ошибка при проверке пароля для пользователя {name}: {e}")
            return False

