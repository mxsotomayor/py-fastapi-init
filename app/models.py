from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, Integer, Table, func
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
    date_updated = Column(DateTime, nullable=False,
                          default=func.now(), onupdate=func.now())


class Feedback(Base):
    """
    SQLAlchemy model for storing user feedback.
    """
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, index=True, nullable=False)
    rating = Column(Integer, nullable=False)  # Rating from 1 to 5
    comment = Column(String, nullable=True)  # Optional comment
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False,
                          default=func.now(), onupdate=func.now())


class Callback(Base):
    """
    SQLAlchemy model for storing callback requests from users.
    """
    __tablename__ = "callbacks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    # e.g., "Morning", "Afternoon", "Anytime"
    contact_period = Column(String, nullable=False)
    # e.g., "Product Inquiry", "Support"
    contact_motive = Column(String, nullable=False)
    observation = Column(String, nullable=True)
    # e.g., "Pending", "Contacted", "Resolved"
    status = Column(String, nullable=False, default="Pending")
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False,
                          default=func.now(), onupdate=func.now())

user_roles_association = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)


class Role(Base):
    """
    SQLAlchemy ORM model for the 'roles' table.
    """
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, unique=True, index=True, nullable=False)
    
    # Define the reverse relationship to User (optional, but good for querying roles and seeing associated users)
    users = relationship("User", secondary=user_roles_association, back_populates="roles")



class User(Base):
    """
    SQLAlchemy ORM model for the 'users' table.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
       # Foreign Key to roles table
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False, default=1) # Default to a 'user' role_id (assuming ID 1 is 'user')

    # Define the relationship to Role
    roles = relationship("Role", secondary=user_roles_association, back_populates="users")



class MyKeys(Base):
    """
    SQLAlchemy model for storing key-value pairs.
    """
    __tablename__ = "my-keys"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_token = Column(String(128), index=True, nullable=False)
    key_value = Column(Integer,  nullable=False)
    email = Column(String(64), nullable=False)
    date_created = Column(DateTime, nullable=False, default=func.now())
    date_updated = Column(DateTime, nullable=False,
                          default=func.now(), onupdate=func.now())
