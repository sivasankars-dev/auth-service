from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.domain.models.refresh_token import RefreshToken
from app.core.config import settings

class RefreshTokenRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_refresh_token(self, user_id: int, token: str) -> RefreshToken:
        expires_at = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at
        )
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token

    def get_by_token(self, token: str) -> RefreshToken:
        return self.db.query(RefreshToken).filter(
            RefreshToken.token == token,
            RefreshToken.revoked == False,
            RefreshToken.expires_at > datetime.utcnow()
        ).first()

    def revoke(self, token: str) -> None:
        refresh_token = self.get_by_token(token)
        if refresh_token:
            refresh_token.revoked = True
            self.db.commit()
