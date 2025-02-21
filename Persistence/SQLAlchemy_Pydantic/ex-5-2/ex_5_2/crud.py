from sqlalchemy.orm import Session
from models import User

# Function to update a user's email
def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return True
    return False