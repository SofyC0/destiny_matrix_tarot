from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin

from app.api.auth_utils import (
    get_password_hash,
    verify_password,
    create_access_token
)

from app.services.matrix_service import calculate_full_matrix

router = APIRouter()


# ==========================================
# REGISTER
# ==========================================

@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    # проверка email
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # проверка username
    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )

    # хэш пароля
    hashed_password = get_password_hash(
        user.password[:72]
    )

    # ==========================================
    # РАСЧЕТ МАТРИЦЫ
    # ==========================================

    matrix_data = calculate_full_matrix(

        day=user.birth_day,

        month=user.birth_month,

        year=user.birth_year
    )

    # ==========================================
    # СОЗДАНИЕ USER
    # ==========================================

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
        "message": "User created successfully",
        "matrix": matrix_data
    }


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(
        user: UserLogin,
        db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

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
        data={
            "sub": db_user.email
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }