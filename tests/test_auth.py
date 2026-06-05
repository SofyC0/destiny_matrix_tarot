# tests/test_auth.py
def test_register_success(client, test_user_data):
    response = client.post("/api/auth/register", json=test_user_data)

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "User created successfully"
    assert "access_token" in data
    assert data["user"]["email"] == test_user_data["email"]
    assert "matrix" in data


def test_register_duplicate_email(client, test_user_data):
    # Первый пользователь
    client.post("/api/auth/register", json=test_user_data)

    # Второй с тем же email
    response = client.post("/api/auth/register", json=test_user_data)

    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_login_success(client, test_user_data):
    # Регистрируем пользователя
    client.post("/api/auth/register", json=test_user_data)

    # Логинимся
    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }

    response = client.post("/api/auth/login", json=login_data)

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_wrong_password(client, test_user_data):
    client.post("/api/auth/register", json=test_user_data)

    response = client.post("/api/auth/login", json={
        "email": test_user_data["email"],
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    assert "Invalid credentials" in response.json()["detail"]