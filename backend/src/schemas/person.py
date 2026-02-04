from pydantic import BaseModel

class PersonLoginSchema(BaseModel):
    username: str
    password: str
    