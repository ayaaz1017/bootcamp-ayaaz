from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User, Post

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Function to insert dummy data
def insert_dummy_data(session: Session):
    if session.query(User).count() == 0:
        # Create dummy users
        user1 = User(name="Alice Smith", email="alice@example.com")
        user2 = User(name="Bob Johnson", email="bob@example.com")

        # Create dummy posts
        post1 = Post(title="First Post", content="This is Alice's first post.", author=user1)
        post2 = Post(title="Second Post", content="This is Alice's second post.", author=user1)
        post3 = Post(title="Bob's Post", content="This is Bob's post.", author=user2)

        # Add and commit dummy data
        session.add_all([user1, user2, post1, post2, post3])
        session.commit()
        print("Dummy data inserted successfully!")
    else:
        print("Database already contains data. Skipping dummy data insertion.")

# Create a new session
with Session(engine) as session:
    # Insert dummy data
    insert_dummy_data(session)