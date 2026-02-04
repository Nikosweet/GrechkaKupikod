from sqlalchemy import select
from typing import Optional, List
import bcrypt
from src.database import session_factory
from src.database.models.person import PersonOrm
from src.schemas import PersonLoginSchema

class PersonService:
    @classmethod
    async def get_persons(cls) -> List[PersonOrm]:
        stmt = select(PersonOrm)
        async with session_factory() as session:
            res = await session.execute(stmt)
            persons = res.scalars().all()

            return persons



    @classmethod
    async def get_person(cls, name: str) -> Optional[PersonOrm]:
        stmt = select(PersonOrm).where(PersonOrm.name == name)
        async with session_factory() as session:
            res = await session.execute(stmt)
            person = res.scalar_one_or_none()
            return person
        


    @classmethod
    async def add_person(cls, person_data: PersonLoginSchema) -> PersonOrm:
        existing_person = await cls.get_person(person_data.name)

        if existing_person:
            raise ValueError(f"Пользователь с именем '{person_data.name}' уже существует")
        
        hashed_password = bcrypt.hashpw(
            person_data.password.encode('utf-8'),
            bcrypt.gensalt(rounds=12)
        ).decode('utf-8')
        
        person = PersonOrm(name=person_data.name, hashpassword=hashed_password)
        async with session_factory() as session:
            session.add(person)
            await session.commit()
            await session.refresh(person)
            return person


    @classmethod
    async def delete_person(cls, name: str) -> bool:
        person_to_delete = await cls.get_person(name)
        if not person_to_delete:
            raise ValueError(f"Пользователь с именем '{name}' не найден")

        async with session_factory() as session:
            person_to_delete = await session.merge(person_to_delete)
            session.delete(person_to_delete)
            await session.commit()
            return True
        




    @classmethod
    async def verify_password(cls, person_data: PersonLoginSchema) -> bool:
        person = await cls.get_person(person_data.name)
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

