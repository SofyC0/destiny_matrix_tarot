# tests/test_matrix.py
import pytest


def test_get_matrix_without_auth(client):
    """Проверка, что без токена нельзя получить матрицу"""
    response = client.get("/api/matrix/me")
    assert response.status_code == 401


def test_get_matrix_after_register(client, test_user_data):
    # Регистрируемся
    register_resp = client.post("/api/auth/register", json=test_user_data)
    token = register_resp.json()["access_token"]

    # Получаем матрицу
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/matrix/me", headers=headers)

    assert response.status_code == 200
    data = response.json()

    assert "matrix" in data
    assert "birth_data" in data["matrix"]
    assert "main_arcana" in data["matrix"]
