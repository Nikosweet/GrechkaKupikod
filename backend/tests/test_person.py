import pytest
import pytest_asyncio
import bcrypt
import asyncio
from pydantic import ValidationError
from database.database import Base, async_engine, session_factory
from database.models.person import PersonOrm
from schemas.person import PersonSchema
from services.person import PersonService

from sqlalchemy.ext.asyncio import create_async_engine


@pytest_asyncio.fixture(loop_scope='function')
async def fixture_persons():
    async with session_factory() as session:
        hashed_password = bcrypt.hashpw(
            '1234'.encode('utf-8'),
            bcrypt.gensalt(rounds=12)
        ).decode('utf-8')

        person1 = PersonOrm(name="fixture_user1", hashpassword=hashed_password)
        person2 = PersonOrm(name="fixture_user2", hashpassword=hashed_password)
        
        session.add_all([person1, person2])
        await session.commit()
        await session.refresh(person1)
        await session.refresh(person2)
        
        return [person1, person2]

@pytest.mark.asyncio
class TestService:
    async def test_get_persons(self):
        fixture_persons = [1,2]
        persons = await PersonService.get_persons()

        persons_sorted = sorted(persons, key=lambda x: x.id)
        fixture_persons_sorted = sorted(fixture_persons, key=lambda x: x.id)

        assert persons_sorted == fixture_persons_sorted


    async def test_get_person(self):
        fixture_persons = [1,2]
        person = await PersonService.get_person('fixture_user1')
        assert person == fixture_persons[0]

    @pytest.mark.parametrize(
    "name, password, should_raise",
    [
        ("aaa", "1234", False),
        ("a"*50, "1234", False),
        ("a"*51, "1234", True),
    ]
    )
    async def test_add_person(self, name, password, should_raise):
        fixture_persons = [1,2]
        try:
            new_person = PersonSchema(name=name, password=password)
        except ValidationError:
            if should_raise:
                return
        added_person = await PersonService.add_person(new_person)
        person = await PersonService.get_person(name)
        assert person == added_person


    async def test_delete_person(self):
        pass

    async def test_update_person(self):
        pass

class TestController:
    pass


