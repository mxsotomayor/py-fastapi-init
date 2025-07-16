# --- Pydantic Schemas ---
# Schema for incoming request data (validation)
from datetime import datetime
from pydantic import BaseModel, EmailStr


class DeviceCreate(BaseModel):
    email: EmailStr
    fbase_token: str

    class Config:
        # Allows ORM models to be converted to Pydantic models
        from_attributes = True

# Schema for outgoing response data (serialization)
class DeviceResponse(BaseModel):
    """
    Pydantic schema for returning device information.
    """
    email: EmailStr
    fbase_token: str
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True