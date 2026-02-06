from authx import AuthX, AuthXConfig
from pydantic_settings import BaseSettings, SettingsConfigDict
from schemas.person import PersonSchema

class JWTSettings(BaseSettings):
    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(env_file='.env')

class AuthService:
    @classmethod
    async def make_config(cls):
        config = AuthXConfig()
        config.JWT_SECRET_KEY=JWTSettings.JWT_SECRET_KEY
        config.JWT_ACCESS_COOKIE_NAME= "access_token"
        config.JWT_TOKEN_LOCATION=["cookies"]
        return AuthX(config=config)

    

    