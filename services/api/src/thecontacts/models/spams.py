from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from thecontacts.data.database.db import base

class Spams(base):
    __tablename__ = 'spams'

    # Generate uuid
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    # Spam's name
    name = Column(String, nullable=True)

    # Spam's phone number
    phone = Column(String, nullable=False)

    # reported on date
    reported_on = Column(String, nullable=False)

