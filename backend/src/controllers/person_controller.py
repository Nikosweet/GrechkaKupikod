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
        @self.router.get("/", response_model=List[PersonResponseSchema])
        async def get_all():
            persons = await PersonService.get_all()
            for person in persons:
                person = PersonResponseSchema.model_validate(person)
            return persons


        @self.router.get("/{person_id}", response_model=PersonResponseSchema)
        async def get(person_id: int):
            person = await PersonService.get(person_id)
            return PersonResponseSchema.model_validate(person)


        @self.router.post("/", response_model=PersonResponseSchema, status_code=status.HTTP_201_CREATED)
        async def add(person: PersonLoginSchema):
            person = await PersonService.add(person)
            return PersonResponseSchema.model_validate(person)

        @self.router.delete("/{person_id}", response_model=bool)
        async def delete(person_id: int):
            return await PersonService.delete(person_id)


        @self.router.put("/{person_id}", response_model=PersonResponseSchema)
        async def update(person_id: int, person: PersonSchema):
            person = await PersonService.update(person_id, person)
            return PersonResponseSchema.model_validate(person)