from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User  # Import the User model
from schemas import UserSchema  # Import the User schema
from crud import get_users

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Function to insert dummy data
def insert_dummy_data(session: Session):
    # Check if the database already has users
    if session.query(User).count() == 0:
        # Create dummy users
        dummy_users = [
            User(name="Alice Smith", email="alice@example.com"),
            User(name="Bob Johnson", email="bob@example.com"),
            User(name="Charlie Brown", email="charlie@example.com"),
        ]

        # Add and commit dummy users to the database
        session.add_all(dummy_users)
        session.commit()
        print("Dummy data inserted successfully!")
    else:
        print("Database already contains data. Skipping dummy data insertion.")

# Create a new session
with Session(engine) as session:
    # Insert dummy data
    insert_dummy_data(session)

    # Fetch all users
    users = get_users(session)

    # Convert SQLAlchemy models to Pydantic schemas
    user_schemas = [UserSchema.from_orm(user) for user in users]

    # Print users in a structured format
    for user in user_schemas:
        print(f"User ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print("-" * 20)