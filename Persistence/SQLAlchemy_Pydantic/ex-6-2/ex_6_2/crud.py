from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema

# Function to fetch a user and their posts
def get_user_with_posts(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return UserSchema.from_orm(user)
    return None