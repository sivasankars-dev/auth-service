from fastapi import HTTPException, status
from app.infrastructure.repositories import UserRepository
from app.utils.security import hash_password, create_access_token, verify_password
from app.schemas.auth import UserCreate, LoginRequest

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, user_data: UserCreate):
        email = user_data.email
        if self.repo.get_by_email(email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        return self.repo.create(
            email=email,
            hashed_password=hash_password(user_data.password)
        )

    def login_user(self, data: LoginRequest):
        user = self.repo.get_by_email(data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        # Token generation logic would go here (omitted for brevity)
        access_token = create_access_token(
            subject=str(user.id)
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }