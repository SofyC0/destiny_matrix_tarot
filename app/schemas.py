from pydantic import BaseModel, EmailStr
from typing import Dict, Any


# ==========================================
# REGISTER
# ==========================================

class UserCreate(BaseModel):

    email: EmailStr

    username: str

    password: str

    # дата рождения
    birth_day: int

    birth_month: int

    birth_year: int


# ==========================================
# LOGIN
# ==========================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str


# ==========================================
# TOKEN
# ==========================================

class Token(BaseModel):

    access_token: str

    token_type: str


# ==========================================
# USER OUT
# ==========================================

class UserOut(BaseModel):

    id: int

    email: str

    username: str

    birth_day: int

    birth_month: int

    birth_year: int

    matrix_data: Dict[str, Any] | None = None

    class Config:
        from_attributes = True