from authx import AuthX, AuthXConfig
from pydantic_settings import BaseSettings, SettingsConfigDict
from schemas.person import PersonSchema

class JWTSettings(BaseSettings):
    JWT_SECRET_KEY: str

    @property
    def get_secret_key():
        return JWT_SECRET_KEY

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

class AuthService:
    @classmethod
    def make_config(cls):
        config = AuthXConfig()
        config.JWT_SECRET_KEY=JWTSettings.get_secret_key
        config.JWT_ACCESS_COOKIE_NAME= "access_token"
        config.JWT_TOKEN_LOCATION=["cookies"]
        return AuthX(config=config)

    

    