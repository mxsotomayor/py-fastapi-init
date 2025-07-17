# --- Pydantic Schemas ---
# Schema for incoming request data (validation)
from datetime import datetime
from typing import List
from fastapi import Query
from pydantic import BaseModel


# Schema for incoming request data (validation) for Callback
class CallbackCreate(BaseModel):
    """
    Pydantic schema for creating a new callback request.
    """
    full_name: str
    phone: str
    contact_period: str
    contact_motive: str
    observation: str | None = None

    class Config:
        from_attributes = True

# Schema for outgoing response data (serialization) for Callback
class CallbackResponse(BaseModel):
    """
    Pydantic schema for returning callback information.
    Includes automatically generated timestamps and status.
    """
    id: int
    full_name: str
    phone: str
    contact_period: str
    contact_motive: str
    observation: str | None
    status: str
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True


class PaginatedCallbacksResponse(BaseModel):
    items: List[CallbackResponse]
    total: int
    page: int
    limit: int

class Paginator:
    def __init__(self, page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
        self.page = page
        self.limit = limit
        self.skip = (page - 1) * limit