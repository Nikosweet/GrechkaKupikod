from fastapi import APIRouter, Depends, HTTPException, status, Response
from schemas.person import PersonResponseSchema, PersonLoginSchema
from database.models.person import PersonOrm
from services.auth_service import AuthService
from authx import TokenPayload

class AuthController:
    def __init__(self):
        self.router = APIRouter(tags=["auth"])
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/login")
        async def login(person: PersonLoginSchema, response: Response):
            return await AuthService.login(person, response)

        @self.router.post("/refresh")
        async def refresh(payload: TokenPayload = Depends(AuthService.security.refresh_token_required), response: Response = None):
            return await AuthService.refresh(payload, response)

    async def verify(person: PersonLoginSchema):
        isVerified = await AuthService.verify(person)
        if isVerified:
            return True
        else:
            return False