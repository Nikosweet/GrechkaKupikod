from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from schemas.person import PersonSchema, PersonResponseSchema, PersonLoginSchema
from services.person_service import PersonService
from database.models.person import PersonOrm



class PersonController:
    def __init__(self):
        self.router = APIRouter(prefix="/users", tags=["users"])
        self._register_routes()

    def _register_routes(self):
        self.router.add_api_route(
            '/',
            self.get_all,
            methods=["GET"],
            response_model=List[PersonSchema]
        )

        self.router.add_api_route(
            '/{person_id}',
            self.get,
            methods=["GET"],
            response_model=PersonSchema
        )

        self.router.add_api_route(
            '/',
            self.add,
            methods=["POST"],
            response_model=PersonSchema,
            status_code=status.HTTP_201_CREATED
        )

        self.router.add_api_route(
            '/{person_id}',
            self.delete,
            methods=["DELETE"],
            response_model=bool
        )

        self.router.add_api_route(
            '/{person_id}',
            self.update,
            methods=["PUT"],
            response_model=PersonSchema
        )

    async def get_all(self):
        persons = await PersonService.get_all()
        for person in persons:
            person = PersonResponseSchema.model_validate(person)
        return persons

    async def get(self, person_id: int):
        person = await PersonService.get(person_id)
        return PersonResponseSchema.model_validate(person)

    async def add(self, person: PersonLoginSchema):
        person = await PersonService.add(person)
        return PersonResponseSchema.model_validate(person)
            

    async def delete(self, person_id: int):
        return await PersonService.delete(person_id)


    async def update(self, person_id: int, person: PersonSchema):
        person = await PersonService.update(person_id, person)
        return PersonResponseSchema.model_validate(person)