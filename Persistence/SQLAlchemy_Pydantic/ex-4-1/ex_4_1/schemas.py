from pydantic import BaseModel

# Pydantic schema for User
class UserSchema(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True  # Enables ORM mode for Pydantic