# --- Pydantic Schemas ---
# Schema for incoming request data (validation)
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, conint


# Schema for incoming request data (validation) for Feedback
class FeedbackCreate(BaseModel):
    """
    Pydantic schema for creating a new feedback entry.
    Validates email format, rating (1-5), and optional comment.
    """
    email: EmailStr
    rating: int = Field(..., description="Rating from 1 to 5")
    comment: str | None = None

    class Config:
        from_attributes = True

# Schema for outgoing response data (serialization) for Feedback
class FeedbackResponse(BaseModel):
    """
    Pydantic schema for returning feedback information.
    Includes automatically generated timestamps.
    """
    id: int
    email: EmailStr
    rating: int
    comment: str | None
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True