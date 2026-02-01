from fastapi import HTTPException, status
from app.infrastructure.user_repo import UserRepository
from app.infrastructure.refresh_token_repo import RefreshTokenRepository
from app.utils.security import hash_password, create_access_token, verify_password, create_refresh_token
from app.schemas.auth import UserCreate, LoginRequest
from app.infrastructure.refresh_token_repo import RefreshTokenRepository

class AuthService:
    def __init__(self, user_repo: UserRepository, refresh_repo: RefreshTokenRepository = None):
        self.user_repo = user_repo
        self.refresh_repo = refresh_repo

    def register_user(self, user_data: UserCreate):
        email = user_data.email
        if self.user_repo.get_by_email(email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        return self.user_repo.create(
            email=email,
            hashed_password=hash_password(user_data.password)
        )

    def login_user(self, data: LoginRequest):
        user = self.user_repo.get_by_email(data.email)
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

        refresh_token = create_refresh_token()
        RefreshTokenRepository.save_refresh_token(self.user_repo, user.id, refresh_token)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    def logout_user(self, refresh_token: str):
        user = self.refresh_repo.get_by_token(refresh_token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid refresh token"
            )
        self.refresh_repo.revoke(refresh_token)
        return True