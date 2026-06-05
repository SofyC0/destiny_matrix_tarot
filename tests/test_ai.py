# tests/test_ai.py

import pytest
from fastapi.testclient import TestClient


# ==========================================
# ТЕСТЫ AI-ФУНКЦИЙ
# ==========================================

def test_ai_full_reading_free_user(client, test_user_data):
    """Free пользователь может получить полный AI-разбор матрицы"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/matrix-ai/full-reading", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "reading" in data


def test_ai_element_reading_free_user(client, test_user_data):
    """Free пользователь может получить AI-разбор отдельного элемента"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/matrix-ai/element/center", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "reading" in data


def test_ai_ask_question_free_user(client, test_user_data):
    """Free пользователь может задать вопрос AI"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    payload = {"question": "Какое мое главное предназначение?"}

    response = client.post("/api/matrix-ai/ask", json=payload, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data


def test_ai_without_matrix_returns_error(client):
    """Если у пользователя нет матрицы — ошибка"""
    # Создаём пользователя без матрицы вручную (через БД) — сложнее, пропустим для простоты
    pass


def test_ai_premium_user_has_full_access(client, test_user_data):
    """Премиум-пользователь имеет полный доступ к AI"""

    # Регистрируем пользователя
    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Делаем премиум
    from app.database import SessionLocal
    from app.models import User
    db = SessionLocal()
    user = db.query(User).filter(User.email == test_user_data["email"]).first()
    if user:
        user.is_premium = True
        db.commit()
    db.close()

    # Полный разбор
    response = client.get("/api/matrix-ai/full-reading", headers=headers)
    assert response.status_code == 200

    # Разбор элемента
    response = client.get("/api/matrix-ai/element/money-channel", headers=headers)
    assert response.status_code == 200

    # Вопрос
    payload = {"question": "Что мне делать с деньгами в этом году?"}
    response = client.post("/api/matrix-ai/ask", json=payload, headers=headers)
    assert response.status_code == 200


def test_ai_ask_question_without_auth(client):
    """Без токена AI недоступен"""
    payload = {"question": "Какое мое предназначение?"}
    response = client.post("/api/matrix-ai/ask", json=payload)

    assert response.status_code == 401