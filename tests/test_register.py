from tests.utils import register_user

def test_register_user_success(client):
    response = register_user(client, "login@example.com")

    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == "login@example.com"

def test_register_duplicate_email(client):
    response = register_user(client, "duplicate@example.com")

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "StrongPass123",
        },
    )

    assert response.status_code == 400
