from pydantic import BaseModel, EmailStr
from typing import Dict, Any


class UserCreate(BaseModel):

    email: EmailStr
    username: str
    password: str
    birth_day: int
    birth_month: int
    birth_year: int


class UserLogin(BaseModel):

    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class UserDataUpdate(BaseModel):
    data: Dict[str, Any]