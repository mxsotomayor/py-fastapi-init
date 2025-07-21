# schemas.py
from typing import List, Optional
from pydantic import BaseModel, EmailStr

# Schema for creating a new user (request body)
class UserCreate(BaseModel):
    """
    Pydantic schema for creating a new user.
    Used for validating incoming request data.
    """
    email: EmailStr # Ensures the email is a valid email format
    password: str
    role_ids: Optional[List[int]] = None # List of role IDs, optional


# Schema for a user response (what is returned by the API)
class UserResponse(BaseModel):
    """
    Pydantic schema for representing a user in API responses.
    """
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        # This tells Pydantic to read the data as an ORM model.
        # It means Pydantic will try to read the data from a SQLAlchemy model
        # or any other ORM, not just a dict.
        orm_mode = True



class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int

    class Config:
        orm_mode = True