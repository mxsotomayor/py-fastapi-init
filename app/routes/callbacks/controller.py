from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.routes.callbacks.schemas import CallbackCreate, CallbackResponse, PaginatedCallbacksResponse, Paginator
from app.routes.callbacks.services import CallbackService

router = APIRouter()

base_path = "/callbacks"


@router.get(base_path, response_model=PaginatedCallbacksResponse, status_code=status.HTTP_200_OK, tags=["Scheduled CallBacks"])
def list_paginated_callbacks(
    paginator: Paginator = Depends(),
    # Assuming get_db is in your services file or a common dependencies file
    db: Session = Depends(get_db)
):
    """
    Endpoint to list paginated callbacks.
    Allows specifying page number and limit for results.
    """
    callback_service = CallbackService()  # Assuming you have a CallbackService

    try:
        total_callbacks = callback_service.count_callbacks(db=db)

        callbacks = callback_service.get_callbacks(
            db=db, skip=paginator.skip, limit=paginator.limit)

        return PaginatedCallbacksResponse(
            items=[callback for callback in callbacks],
            total=total_callbacks,
            page=paginator.page,
            limit=paginator.limit
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving callbacks: {e}"
        )


@router.post(base_path, response_model=CallbackResponse, status_code=status.HTTP_201_CREATED, tags=["Scheduled CallBacks"])
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
        db_callback = callback_service.create_callback(
            db=db, callback=callback)
        return db_callback
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while submitting the callback request: {e}"
        )
