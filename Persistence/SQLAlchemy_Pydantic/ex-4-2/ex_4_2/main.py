from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User
from schemas import UserCreate
from crud import create_user

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Create a new session
with Session(engine) as session:
    # Create a new user
    new_user = UserCreate(name="Jane Doe", email="jane@example.com")
    created_user = create_user(session, new_user)
    print(f"Created user: {created_user.name} ({created_user.email})")