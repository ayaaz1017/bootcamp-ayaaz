from pydantic import BaseModel, EmailStr

# Pydantic schema for User creation
class UserCreate(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # Enables ORM mode for Pydantic