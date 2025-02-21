from pydantic import BaseModel, EmailStr

# Pydantic schema for User
class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True