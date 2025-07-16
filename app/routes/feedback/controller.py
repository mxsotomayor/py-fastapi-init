from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.routes.feedback.schemas import FeedbackCreate, FeedbackResponse
from app.routes.feedback.services import  FeedbackService

router = APIRouter()

base_path = "/feedback"

@router.post(base_path, response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED, tags=["Customer Feedback"])
def submit_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    """
    Endpoint to submit user feedback.
    Accepts an email, a rating (1-5), and an optional comment.
    """
    feedback_service = FeedbackService()
    try:
        db_feedback = feedback_service.create_feedback(db=db, feedback=feedback)
        return db_feedback
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while submitting feedback: {e}"
        )
    
    