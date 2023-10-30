from typing import Optional

from pydantic import BaseModel


class BlogSchema(BaseModel):
    user_id: int
    title: str
    description: str

    class Config():
        orm_mode = True


class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
