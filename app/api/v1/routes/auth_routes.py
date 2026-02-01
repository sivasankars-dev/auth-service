from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import UserCreate, UserResponse, LogoutRequest
from app.api.v1.dependencies import get_db, get_current_user
from app.infrastructure.user_repo import UserRepository
from app.infrastructure.refresh_token_repo import RefreshTokenRepository
from app.services.auth_service import AuthService
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)

    return service.register_user(user)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)
    res = service.login_user(data)
    print(res)
    return res

@router.post("/logout", dependencies=[Depends(get_current_user)])
def logout_user(
    payload: LogoutRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_repo = UserRepository(db)
    refresh_repo = RefreshTokenRepository(db)
    service = AuthService(user_repo, refresh_repo)

    service.logout_user(payload.refresh_token)
    return {"detail": "Successfully logged out"}

@router.get("/protected")
def protected_endpoint(current_user=Depends(get_current_user)):
    return {"detail": f"Hello, {current_user.email}. You have accessed a protected endpoint."}