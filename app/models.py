from datetime import datetime
import uuid
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String, Date, Float, Integer, Double, JSON, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# --- SQLAlchemy Model ---
class Device(Base):
    """
    SQLAlchemy model for storing mobile device information.
    """
    __tablename__ = "devices"

    email = Column(String, primary_key=True, index=True)
    fbase_token = Column(String, unique=True, index=True, nullable=False)
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class Feedback(Base):
    """
    SQLAlchemy model for storing user feedback.
    """
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, index=True, nullable=False)
    rating = Column(Integer, nullable=False) # Rating from 1 to 5
    comment = Column(String, nullable=True) # Optional comment
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class Callback(Base):
    """
    SQLAlchemy model for storing callback requests from users.
    """
    __tablename__ = "callbacks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    contact_period = Column(String, nullable=False) # e.g., "Morning", "Afternoon", "Anytime"
    contact_motive = Column(String, nullable=False) # e.g., "Product Inquiry", "Support"
    observation = Column(String, nullable=True)
    status = Column(String, nullable=False, default="Pending") # e.g., "Pending", "Contacted", "Resolved"
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

