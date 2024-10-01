from pydantic import BaseModel, EmailStr
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(Post):
    pass


class PostResponse(Post):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserResp(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
