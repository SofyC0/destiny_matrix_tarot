from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean, Text, Float
from sqlalchemy.sql import func
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    # Основные поля
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # Данные пользователя
    full_name = Column(String(200), nullable=True)
    avatar_url = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # JSON поля для хранения сложных данных
    user_data = Column(JSON, default=dict)  # Здесь хранится матрица судьбы
    tarot_readings = Column(JSON, default=list)  # История раскладов таро
    settings = Column(JSON, default=dict)  # Настройки пользователя

    # Даты
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)

    # Дополнительная статистика
    total_calculations = Column(Integer, default=0)

    def __repr__(self):
        return f"<User {self.username}>"


class CalculationHistory(Base):
    __tablename__ = "calculation_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    calculation_type = Column(String(50))  # 'matrix' или 'tarot'
    input_data = Column(JSON)  # Входные данные (дата рождения, вопрос и т.д.)
    result_data = Column(JSON)  # Результат расчёта
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class SessionToken(Base):
    __tablename__ = "session_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    token = Column(String(500), unique=True, index=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_revoked = Column(Boolean, default=False)