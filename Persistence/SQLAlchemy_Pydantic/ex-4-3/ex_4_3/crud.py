from sqlalchemy.orm import Session
from models import User  # Import the User model, not the schema
from schemas import UserSchema  # Import the schema for type hints (optional)

# Function to fetch all users
def get_users(db: Session):
    return db.query(User).all()