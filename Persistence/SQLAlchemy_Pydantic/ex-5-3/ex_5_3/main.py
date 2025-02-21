from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User
from crud import delete_user

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

    # Delete a user
    user_id_to_delete = 1
    if delete_user(session, user_id_to_delete):
        print(f"User {user_id_to_delete} deleted successfully!")
    else:
        print(f"No user found with ID: {user_id_to_delete}")