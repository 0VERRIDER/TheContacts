from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..data.database.db import Base

class Users(Base):
    __tablename__ = 'users'

    # Generate uuid
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    # User's name
    name = Column(String, nullable=False)

    # User's phone number
    phone = Column(String, nullable=False, unique=True)

    # User's password
    password = Column(String, nullable=False)

    # User's email
    email = Column(String, nullable=True)

