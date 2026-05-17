from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models import User

from app.schemas import UserCreate
from app.schemas import UserLogin

from app.users import get_user_by_email
from app.users import get_user_by_username

from app.routers.auth_utils import (
    get_password_hash,
    verify_password,
    create_access_token
)

from app.services.matrix_service import calculate_matrix

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    existing_email = get_user_by_email(
        db,
        user.email
    )

    if existing_email:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    existing_username = get_user_by_username(
        db,
        user.username
    )

    if existing_username:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = get_password_hash(
        user.password[:72]
    )

    matrix_data = calculate_matrix(
        user.birth_day,
        user.birth_month,
        user.birth_year
    )

    new_user = User(

        email=user.email,

        username=user.username,

        hashed_password=hashed_password,

        birth_day=user.birth_day,

        birth_month=user.birth_month,

        birth_year=user.birth_year,

        matrix_data=matrix_data
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created",
        "matrix": matrix_data
    }


@router.post("/login")
def login(
        user: UserLogin,
        db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
            user.password,
            db_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }