# app/api/matrix.py

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User

from app.api.auth_utils import get_current_user
from app.services.matrix_geometry_service import build_matrix_geometry

from app.services.matrix_interpreter import (
    interpret_center,
    interpret_business_card,
    interpret_money_channel,
    interpret_love_channel,
    interpret_destinations,
    interpret_generation_lines,
    interpret_karma_tail,
    interpret_age_arcana,
    generate_full_matrix_reading
)

router = APIRouter()


# =========================================================
# DB
# =========================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# =========================================================
# ВСЯ МАТРИЦА
# =========================================================

@router.get("/me")

def get_my_matrix(

    current_user: User = Depends(get_current_user)
):

    return current_user.matrix_data


# =========================================================
# ПОЛНЫЙ РАЗБОР
# =========================================================

@router.get("/reading")

def get_full_reading(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return generate_full_matrix_reading(matrix)


# =========================================================
# ЦЕНТР
# =========================================================

@router.get("/element/center")

def get_center(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_center(matrix)


# =========================================================
# ВИЗИТКА
# =========================================================

@router.get("/element/business-card")

def get_business_card(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_business_card(matrix)


# =========================================================
# КАНАЛ ДЕНЕГ
# =========================================================

@router.get("/element/money-channel")

def get_money_channel(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_money_channel(matrix)


# =========================================================
# КАНАЛ ЛЮБВИ
# =========================================================

@router.get("/element/love-channel")

def get_love_channel(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_love_channel(matrix)


# =========================================================
# ПРЕДНАЗНАЧЕНИЯ
# =========================================================

@router.get("/element/destinations")

def get_destinations(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_destinations(matrix)


# =========================================================
# РОДОВЫЕ ЛИНИИ
# =========================================================

@router.get("/element/generation-lines")

def get_generation_lines(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_generation_lines(matrix)


# =========================================================
# КАРМИЧЕСКИЙ ХВОСТ
# =========================================================

@router.get("/element/karma-tail")

def get_karma_tail(

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    return interpret_karma_tail(matrix)


# =========================================================
# АРКАН НА ВОЗРАСТ
# =========================================================

@router.get("/age/{age}")

def get_age_arcana(

    age: int,

    current_user: User = Depends(get_current_user)
):

    matrix = current_user.matrix_data

    result = interpret_age_arcana(

        matrix,
        age
    )

    if not result:

        raise HTTPException(

            status_code=404,

            detail="Возраст не найден"
        )

    return result

@router.get("/geometry")
def get_geometry():

    matrix = build_matrix_geometry(
        2,
        3,
        2005
    )

    return matrix