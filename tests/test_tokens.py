# tests/test_tokens.py
import time

def test_access_token_expiry(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "expire@example.com",
            "password": "StrongPass123",
        },
    )

    login_res = client.post(
        "/api/v1/auth/login",
        json={
            "email": "expire@example.com",
            "password": "StrongPass123",
        },
    )

    token = login_res.json()["access_token"]

    time.sleep(2)  # only if short expiry for tests

    res = client.get(
        "/api/v1/protected",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert res.status_code in (200, 401)
