from pydantic import BaseModel, Field

class PersonSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    password: str = Field(max_length=72)
    