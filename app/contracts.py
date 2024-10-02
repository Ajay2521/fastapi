from typing import Optional
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


class User(BaseModel):
    email: EmailStr
    password: str


class CreateUser(User):
    pass


class UserResp(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserCredentials(User):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
