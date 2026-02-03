from database import session_factory
from database.models.user import PersonOrm

async def add_person(name, password):
    person = PersonOrm(name, password)
    async with session_factory() as session:
        session.add(person)
        await session.commit()

add_person("Nikolay", "12345")