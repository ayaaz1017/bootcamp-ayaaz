from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User
from crud import bulk_insert_users

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Create a new session
with Session(engine) as session:
    # Data for bulk insert
    users_data = [
        {"name": "Alice Smith", "email": "alice@example.com"},
        {"name": "Bob Johnson", "email": "bob@example.com"},
        {"name": "Charlie Brown", "email": "charlie@example.com"},
    ]

    # Perform bulk insert
    bulk_insert_users(session, users_data)