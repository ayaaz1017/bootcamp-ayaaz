from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ex_4_3.models import Base, User
from ex_4_3.crud import get_users

# Test database URL
TEST_DATABASE_URL = "sqlite:///./test.db"

# Create a test engine and session
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

def test_get_users():
    # Add a test user to the database
    with Session(engine) as session:
        test_user = User(name="Test User", email="test@example.com")
        session.add(test_user)
        session.commit()

    # Fetch all users
    with Session(engine) as session:
        users = get_users(session)
        assert len(users) >= 1
        assert users[0].name == "Test User"
        assert users[0].email == "test@example.com"