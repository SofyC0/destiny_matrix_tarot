from pydantic import BaseModel
from pydantic import EmailStr


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


class TarotRequest(BaseModel):

    spread_type: str


class AIQuestionRequest(BaseModel):

    question: str


class MatrixElementRequest(BaseModel):

    element_name: str