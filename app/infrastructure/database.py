from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.core.config import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()