from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserLogin

from app.api.auth_utils import (
    get_password_hash,
    authenticate_user,
    create_access_token
)

from app.services.matrix_elements_service import (
    calculate_full_matrix
)

router = APIRouter()


# =====================================================
# DB
# =====================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =====================================================
# REGISTER
# =====================================================

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
            detail="Username already exists"
        )

    # hash password
    hashed_password = get_password_hash(
        user.password
    )

    # MATRIX
    matrix_data = calculate_full_matrix(
        user.birth_day,
        user.birth_month,
        user.birth_year
    )

    # user
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

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {

        "message": "User created successfully",

        "access_token": access_token,

        "matrix": matrix_data
    }


# =====================================================
# LOGIN
# =====================================================

@router.post("/login")
def login(
        user: UserLogin,
        db: Session = Depends(get_db)
):

    auth_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not auth_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={
            "sub": auth_user.email
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }