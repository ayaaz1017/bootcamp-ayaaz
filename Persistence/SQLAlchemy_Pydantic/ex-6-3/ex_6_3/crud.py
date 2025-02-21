from sqlalchemy.orm import Session
from models import User

# Function to insert multiple users
def bulk_insert_users(db: Session, users_data: list):
    try:
        # Begin a transaction
        db.begin()
        for user_data in users_data:
            user = User(name=user_data["name"], email=user_data["email"])
            db.add(user)
        db.commit()
        print("Bulk insert successful!")
    except Exception as e:
        # Rollback on failure
        db.rollback()
        print(f"Bulk insert failed: {e}")