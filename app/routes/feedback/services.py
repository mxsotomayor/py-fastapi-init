from sqlalchemy.orm import Session
from app.models import Feedback
from app.routes.feedback.schemas import FeedbackCreate
class FeedbackService:
    """
    Service layer to encapsulate business logic for feedback operations.
    Handles database interactions.
    """
    def create_feedback(self, db: Session, feedback: FeedbackCreate) -> Feedback:
        """
        Saves new user feedback to the database.
        """
        new_feedback = Feedback(
            email=feedback.email,
            rating=feedback.rating,
            comment=feedback.comment
        )
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        return new_feedback