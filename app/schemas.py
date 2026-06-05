from typing import (
    Any,
    Dict,
    Optional
)

from pydantic import (

    BaseModel,

    ConfigDict,

    EmailStr,

    Field,

    field_validator
)


# ==========================================
# BASE USER
# ==========================================

class UserBase(BaseModel):

    email: EmailStr

    username: str = Field(

        min_length=3,

        max_length=30
    )

    @field_validator("username")
    @classmethod
    def validate_username(
            cls,
            value: str
    ):

        value = value.strip()

        if not value:

            raise ValueError(
                "Username cannot be empty"
            )

        return value


# ==========================================
# REGISTER
# ==========================================

class UserCreate(UserBase):

    password: str = Field(

        min_length=6,

        max_length=72
    )

    # birth date
    birth_day: int = Field(

        ge=1,

        le=31
    )

    birth_month: int = Field(

        ge=1,

        le=12
    )

    birth_year: int = Field(

        ge=1900,

        le=2100
    )

    @field_validator("password")
    @classmethod
    def validate_password(
            cls,
            value: str
    ):

        value = value.strip()

        if len(value) < 6:

            raise ValueError(
                "Password too short"
            )

        return value


# ==========================================
# LOGIN
# ==========================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str = Field(

        min_length=1,

        max_length=72
    )


# ==========================================
# TOKEN
# ==========================================

class Token(BaseModel):

    access_token: str

    token_type: str


# ==========================================
# TOKEN PAYLOAD
# ==========================================

class TokenPayload(BaseModel):

    sub: str

    exp: int


# ==========================================
# USER RESPONSE
# ==========================================

class UserOut(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    email: EmailStr

    username: str

    is_premium: bool

    birth_day: Optional[int] = None

    birth_month: Optional[int] = None

    birth_year: Optional[int] = None

    matrix_data: Optional[
        Dict[str, Any]
    ] = None


# ==========================================
# AUTH RESPONSE
# ==========================================

class AuthResponse(BaseModel):

    access_token: str

    token_type: str

    user: UserOut