from sqlalchemy import create_engine
from models import Base, User

# Initialize the database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database and tables created successfully!")