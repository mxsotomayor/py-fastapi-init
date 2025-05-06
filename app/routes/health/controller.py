from fastapi import APIRouter
from datetime import datetime


router = APIRouter()


@router.get("/health", tags=["_Health"])
def health_action():
    return {
        "health": True,
        "time": datetime.now()
    }
