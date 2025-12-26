# app/db/base.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from ..core.config import settings


# Load environment variables from .env file
load_dotenv()

# Database URL from environment variables
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy engine: establishes connection to the database
engine = create_engine(
    DATABASE_URL, pool_pre_ping=True  # Prevent connection timeout errors
)

# SessionLocal: factory for creating new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()


# Dependency function for FastAPI routes
def get_db():
    """
    Yield a database session to be used in FastAPI Depends().
    Automatically closes the session after request.

    Example usage in a route:
        def read_users(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
