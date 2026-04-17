from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from datetime import date
from database import SessionLocal
from models import User
from .auth_utils import authenticate_user, create_access_token  # ← Лерины функции

router = APIRouter()


# ==================== Схемы ====================
class UserRegister(BaseModel):
    name: str
    username: str
    password: str
    birth_date: date


class UserLogin(BaseModel):
    username: str
    password: str


# ==================== Эндпоинты ====================
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegister):
    db = SessionLocal()
    try:
        # Проверка, существует ли пользователь
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Пользователь уже существует")

        # Здесь потом добавим расчёт матрицы
        new_user = User(
            username=user.username,
            name=user.name,
            birth_date=user.birth_date,
            hashed_password=user.password  # потом захэшируем
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "Регистрация прошла успешно",
            "user_id": new_user.id,
            "name": new_user.name
        }
    finally:
        db.close()


@router.post("/login")
async def login(user: UserLogin):
    db = SessionLocal()
    try:
        authenticated_user = authenticate_user(db, user.username, user.password)
        if not authenticated_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный логин или пароль"
            )

        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    finally:
        db.close()