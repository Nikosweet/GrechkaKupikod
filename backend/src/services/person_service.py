from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
import bcrypt
from database.database import session_factory
from database.models.person import PersonOrm
from schemas.person import PersonLoginSchema, PersonSchema

class PersonService:
    @classmethod
    async def get_all(cls, session: AsyncSession) -> List[PersonOrm]:
        stmt = select(PersonOrm)
        res = await session.execute(stmt)
        persons = res.scalars().all()

        return persons



    @classmethod
    async def get(cls, id: int, session: AsyncSession) -> Optional[PersonOrm]:
        stmt = select(PersonOrm).where(PersonOrm.id == id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
        


    @classmethod
    async def add(cls, person_data: PersonLoginSchema, session: AsyncSession) -> PersonOrm:
        stmt = select(PersonOrm).where(PersonOrm.name == person_data.name)
        
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
    async def delete(cls, id: int, session: AsyncSession) -> bool:
        person = await cls.get(id, session=session)
        
        if not person:
            return False
        
        await session.delete(person)
        await session.commit()
        return True
    
    @classmethod 
    async def update(cls, id: int, new_data: PersonSchema, session: AsyncSession):
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





