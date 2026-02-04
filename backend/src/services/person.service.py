from src.database import session_factory
from src.database.models.person import PersonOrm

async def add_person(name, password):
    person = PersonOrm(name, password)
    async with session_factory() as session:
        session.add(person)
        await session.commit()

