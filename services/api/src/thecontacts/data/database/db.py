from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import configs
from .config import POSTGRES_SQLALCHEMY_DATABASE_URI

# Create Alchemy engine
engine = create_engine(POSTGRES_SQLALCHEMY_DATABASE_URI)

# Create a local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





