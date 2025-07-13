from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.routes.callbacks.schemas import CallbackCreate, CallbackResponse
from app.routes.callbacks.services import CallbackService
 
router = APIRouter()

base_path = "/callbacks"

@router.post(base_path, response_model=CallbackResponse, status_code=status.HTTP_201_CREATED)
def submit_feedback(
    callback: CallbackCreate,
    db: Session = Depends(get_db)
):
    """
    Endpoint to submit user feedback.
    Accepts an email, a rating (1-5), and an optional comment.
    """
    callback_service = CallbackService()
    try:
        db_callback = callback_service.create_callback(db=db, callback=callback)
        return db_callback
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while submitting the callback request: {e}"
        )
    
    