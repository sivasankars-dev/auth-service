from tests.utils import register_user, login_user

def test_logout_revokes_refresh_token(client):
    register_user(client, "logout@example.com")
    login_res = login_user(client, "logout@example.com")

    refresh_token = login_res.json()["refresh_token"]

    logout_res = client.post(
        "/api/v1/auth/logout",
        json={"refresh_token": refresh_token},
    )

    assert logout_res.status_code == 200

def test_logout_with_invalid_token(client):
    invalid_token = "invalid.token.string"

    logout_res = client.post(
        "/api/v1/auth/logout",
        json={"refresh_token": invalid_token},
    )

    assert logout_res.status_code == 400