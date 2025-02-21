from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Pydantic schema for User
class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # Enables ORM mode for Pydantic

# Pydantic schema for Post
class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    class Config:
        from_attributes = True