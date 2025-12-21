from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.core.settings import settings

DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()