# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
import os

# Тестовая БД
TEST_DATABASE_URL = "sqlite:///./test_users.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Переопределяем зависимость get_db для тестов
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    """Создаёт тестового клиента"""
    Base.metadata.create_all(bind=engine)   # создаём таблицы перед тестом
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)     # чистим после теста


@pytest.fixture(scope="function")
def test_user_data():
    return {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "password123",
        "birth_day": 15,
        "birth_month": 6,
        "birth_year": 2000
    }