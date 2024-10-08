from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class User(BaseModel):
    email: EmailStr
    password: str


class CreateUser(User):
    pass


class UserResp(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCredentials(User):
    pass


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(Post):
    pass


class PostResponse(Post):
    id: int
    created_at: datetime
    user_id: int
    user: UserResp

    model_config = ConfigDict(from_attributes=True)


class PostLikeResponse(BaseModel):
    Post: PostResponse
    Likes: int

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Like(BaseModel):
    post_id: int
