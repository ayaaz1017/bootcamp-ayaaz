from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema

# Function to fetch a user by email
def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return UserSchema.from_orm(user)
    return None