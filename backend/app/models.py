from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    ForeignKey,
    Boolean
)

from sqlalchemy.sql import func

from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)

    username = Column(String, unique=True, index=True)

    hashed_password = Column(String)

    # дата рождения
    birth_day = Column(Integer)

    birth_month = Column(Integer)

    birth_year = Column(Integer)

    # матрица судьбы
    matrix_data = Column(JSON)

    def __repr__(self):
        return f"<User {self.username}>"

# Остальные модели (CalculationHistory, SessionToken) оставьте без изменений, но тоже исправьте импорт Base


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