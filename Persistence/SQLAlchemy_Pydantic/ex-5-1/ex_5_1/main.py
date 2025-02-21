from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User
from schemas import UserSchema
from crud import get_user_by_email

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Function to insert dummy data
def insert_dummy_data(session: Session):
    if session.query(User).count() == 0:
        dummy_users = [
            User(name="Alice Smith", email="alice@example.com"),
            User(name="Bob Johnson", email="bob@example.com"),
            User(name="Charlie Brown", email="charlie@example.com"),
        ]
        session.add_all(dummy_users)
        session.commit()
        print("Dummy data inserted successfully!")
    else:
        print("Database already contains data. Skipping dummy data insertion.")

# Create a new session
with Session(engine) as session:
    # Insert dummy data
    insert_dummy_data(session)

    # Fetch a user by email
    email_to_search = "alice@example.com"
    user = get_user_by_email(session, email_to_search)

    if user:
        print(f"User found: {user.name} ({user.email})")
    else:
        print(f"No user found with email: {email_to_search}")