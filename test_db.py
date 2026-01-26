# test_db.py
from app.infrastructure.database import engine, Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")