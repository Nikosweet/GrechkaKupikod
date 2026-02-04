from pydantic import BaseModel, Field

class PersonLoginSchema(BaseModel):
    name: str = Field(min_length=3, max_length=25)
    password: str = Field(max_length=72)
    