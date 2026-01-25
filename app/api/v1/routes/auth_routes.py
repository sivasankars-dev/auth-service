from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import UserCreate, UserResponse
from app.api.v1.dependencies import get_db
from app.infrastructure.repositories import UserRepository
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)

    if repo.get_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    return service.register_user(user.email, user.password)
