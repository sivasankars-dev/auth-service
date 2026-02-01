def register_user(client, email="test@example.com", password="StrongPass123"):
    return client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": password,
        },
    )


def login_user(client, email="test@example.com", password="StrongPass123"):
    return client.post(
        "/api/v1/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )


def get_auth_headers(access_token: str):
    return {
        "Authorization": f"Bearer {access_token}"
    }
