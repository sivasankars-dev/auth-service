from tests.utils import register_user, login_user

def test_login_success(client):
    register_user(client, "login@example.com")

    response = login_user(client, "login@example.com")

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_login_wrong_password(client):
    register_user(client, "login@example.com")

    response = login_user(client, "login@example.com", "WrongPass123")

    assert response.status_code == 401

