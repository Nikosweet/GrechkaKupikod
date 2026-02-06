from pydantic import BaseModel, Field

class PersonSchema(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    email: str | None = Field(None, min_length=3, max_length=50)
    phone: str | None = Field(None, min_length=5, max_length=15)

    
class PersonLoginSchema(BaseModel):
    name: str = Field(None, min_length=3, max_length=50)
    password: str = Field(max_length=72)
