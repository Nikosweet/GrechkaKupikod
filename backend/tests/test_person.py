import pytest
from contextlib import nullcontext
from src.services.person import add_person

class TestService:
    @pytest.mark.parametrize(
    "name, password, expectation",
    [
        ("aaa", "1234", nullcontext()),
        ("aaaaaaaaaaaaaaaaaaaaaaaaa", "1234", nullcontext()),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaa", "1234", pytest.raises(ValueError)),
    ]
    )
    async def test_add_person(self, name, password, expectation):
        with expectation:
            pass

class TestController:
    pass