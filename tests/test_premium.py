# tests/test_premium.py

import pytest
from fastapi.testclient import TestClient
from app.models import User


# ==========================================
# ТЕСТЫ ПРЕМИУМ-ФУНКЦИЙ
# ==========================================

def test_free_user_cannot_access_premium_matrix_element(client, test_user_data):
    """Free пользователь не может получить премиум-элемент матрицы"""

    # Регистрируем обычного пользователя
    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Пытаемся получить премиум-элемент (например, money_channel)
    response = client.get("/api/matrix/element/money-channel", headers=headers)

    assert response.status_code == 403
    assert "Premium required" in response.json()["detail"]


def test_free_user_can_access_free_matrix_element(client, test_user_data):
    """Free пользователь может получить бесплатные элементы"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/matrix/element/center", headers=headers)

    assert response.status_code == 200
    assert "interpretation" in response.json()


def test_premium_user_can_access_premium_features(client, test_user_data):
    """Премиум-пользователь имеет доступ ко всем функциям"""

    # Регистрируем пользователя
    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Делаем пользователя премиум (через БД)
    from app.database import SessionLocal
    from app.models import User

    db = SessionLocal()
    user = db.query(User).filter(User.email == test_user_data["email"]).first()
    user.is_premium = True
    db.commit()
    db.close()

    # Проверяем доступ к премиум-элементу
    response = client.get("/api/matrix/element/money-channel", headers=headers)
    assert response.status_code == 200


def test_free_user_limited_tarot_spreads(client, test_user_data):
    """Free пользователь может использовать только бесплатные расклады"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Бесплатный расклад
    response = client.get("/api/tarot/card-of-day", headers=headers)
    assert response.status_code == 200

    # Премиум-расклад (должен быть заблокирован)
    response = client.get("/api/tarot/celtic-cross", headers=headers)
    assert response.status_code == 403
    assert "Premium subscription required" in response.json()["detail"]


def test_premium_user_can_use_all_tarot_spreads(client, test_user_data):
    """Премиум-пользователь может использовать все расклады"""

    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Делаем премиум
    from app.database import SessionLocal
    from app.models import User
    db = SessionLocal()
    user = db.query(User).filter(User.email == test_user_data["email"]).first()
    user.is_premium = True
    db.commit()
    db.close()

    # Премиум-расклад
    response = client.get("/api/tarot/celtic-cross", headers=headers)
    assert response.status_code == 200


def test_free_user_ai_limit(client, test_user_data):
    """Free пользователь имеет лимит на AI-запросы"""
    # Этот тест можно расширить позже, когда будет счётчик запросов
    pass


# ==========================================
# ВСПОМОГАТЕЛЬНЫЙ ФИКСТУРА ДЛЯ ПРЕМИУМ-ПОЛЬЗОВАТЕЛЯ
# ==========================================

@pytest.fixture
def premium_user_client(client, test_user_data):
    """Фикстура — зарегистрированный премиум-пользователь"""
    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]

    # Делаем премиум
    from app.database import SessionLocal
    from app.models import User
    db = SessionLocal()
    user = db.query(User).filter(User.email == test_user_data["email"]).first()
    if user:
        user.is_premium = True
        db.commit()
    db.close()

    headers = {"Authorization": f"Bearer {token}"}
    return client, headers