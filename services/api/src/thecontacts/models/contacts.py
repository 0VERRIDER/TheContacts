from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from thecontacts.data.database.db import base

class Contacts(base):
    __tablename__ = 'contacts'

    # Generate uuid
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    # Contact's name
    name = Column(String, nullable=False)

    # Contact's phone number
    phone = Column(String, nullable=False)

    # Contact's email
    email = Column(String, nullable=True)

    # Contact's owner
    owner = Column(UUID(as_uuid=True), nullable=False)

