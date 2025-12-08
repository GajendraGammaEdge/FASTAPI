from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database URL
POSTGRES_URL = "postgresql+psycopg2://postgres:12345@db:5432/cnn"

# SQLAlchemy engine
engine = create_engine(POSTGRES_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
