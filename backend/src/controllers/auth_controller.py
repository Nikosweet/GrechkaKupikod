from fastapi import APIRouter, Depends, HTTPException, status, Response
from schemas.person import PersonResponseSchema, PersonLoginSchema
from database.models.person import PersonOrm
from services.auth_service import AuthService
from authx import TokenPayload
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession


class AuthController:
    def __init__(self):
        self.router = APIRouter(tags=["auth"])
        self._register_routes()

    def _register_routes(self):
        @self.router.post("/login")
        async def login(person: PersonLoginSchema, response: Response, session: AsyncSession = Depends(get_session)):
            return await AuthService.login(person, response, session)

        @self.router.post("/refresh")
        async def refresh(payload: TokenPayload = Depends(AuthService.security.refresh_token_required), response: Response = None):
            return await AuthService.refresh(payload, response)

        @self.router.post('/logout')
        async def logout(response: Response):
            return await AuthService.logout(response)

    async def verify(person: PersonLoginSchema):
        isVerified = await AuthService.verify(person)
        if isVerified:
            return True
        else:
            return False