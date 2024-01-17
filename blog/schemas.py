from typing import List

from pydantic import BaseModel


class BaseBlog(BaseModel):
    title: str
    body: str


class Blog(BaseBlog):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseBlog):
    title: str
    body: str
    creator: User

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
