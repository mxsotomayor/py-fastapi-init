# --- Pydantic Schemas ---
# Schema for incoming request data (validation)
from datetime import datetime
from pydantic import BaseModel, EmailStr


class MyKeyConfirm(BaseModel):
    user_token: str
    indexes: int
    key_value: int

    class Config:
        # Allows ORM models to be converted to Pydantic models
        from_attributes = True

class MyKeyCreate(BaseModel):
    email: EmailStr
    key_value: int

    class Config:
        # Allows ORM models to be converted to Pydantic models
        from_attributes = True

# Schema for outgoing response data (serialization)
class MyKeyResponse(BaseModel):
    """
    Pydantic schema for returning device information.
    """
    email: EmailStr
    key_value: int
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True