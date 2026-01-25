from app.infrastructure.repositories import UserRepository
from app.domain.models import User
from app.utils.security import hash_password

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, email: str, password: str):
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        return self.repo.create(user)
