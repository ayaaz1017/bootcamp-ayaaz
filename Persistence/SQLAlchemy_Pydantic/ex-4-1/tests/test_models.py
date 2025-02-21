from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ex_4_1.models import Base, User

# Test database URL
TEST_DATABASE_URL = "sqlite:///./test.db"

# Create a test engine and session
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

def test_user_model():
    # Create a new user
    user = User(name="John Doe", email="john@example.com")

    # Add the user to the database
    with Session(engine) as session:
        session.add(user)
        session.commit()

    # Verify the user was added
    with Session(engine) as session:
        retrieved_user = session.query(User).filter(User.email == "john@example.com").first()
        assert retrieved_user is not None
        assert retrieved_user.name == "John Doe"