from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import UserCreate, UserResponse
from app.api.v1.dependencies import get_db
from app.infrastructure.repositories import UserRepository
from app.services.auth_service import AuthService
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

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

    return service.login_user(data)
