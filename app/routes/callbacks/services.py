from sqlalchemy.orm import Session
from app.models import Callback, Feedback
from app.routes.callbacks.schemas import CallbackCreate
# --- Service Layer ---
class CallbackService:
    """
    Service layer to encapsulate business logic for callback operations.
    Handles database interactions.
    """
    def create_callback(self, db: Session, callback: CallbackCreate) -> Callback:
        """
        Saves a new callback request to the database.
        """
        new_callback = Callback(
            full_name=callback.full_name,
            phone=callback.phone,
            contact_period=callback.contact_period,
            contact_motive=callback.contact_motive,
            observation=callback.observation,
            status="Pending" # Default status for a new callback
        )
        db.add(new_callback)
        db.commit()
        db.refresh(new_callback)
        return new_callback