import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from app.main import app
from app.infrastructure.database import Base
from sqlalchemy.orm import sessionmaker
from app.api.v1.dependencies import get_db

# Create a test database engine
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def create_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture()
def client(create_test_db):
    return TestClient(app)
