from pydantic import BaseModel, EmailStr
from typing import List

# Pydantic schema for Post
class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True

# Pydantic schema for User
class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    posts: List[PostSchema]  # Nested posts

    class Config:
        from_attributes = True