import uuid
from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    document_type = Column(String, nullable=False)
    document_number = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
