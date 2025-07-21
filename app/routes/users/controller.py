

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User
from app.routes.users import schemas
from app.routes.users.services import UserService
from app.routes.users.schemas import UserResponse


router = APIRouter()

base_path = "/users"

@router.post(base_path, response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db) # Inject database session
):
    """
    Create a new user.
    Checks if a user with the given email already exists.
    """
    service = UserService()
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
   
    # Create the user using the service layer
    new_user = service.create_user(db=db, user=user)
    return new_user

@router.get(f"{base_path}/{{user_id}}", response_model=schemas.UserResponse, tags=["Users"])
def read_user(
    user_id: int,
    db: Session = Depends(get_db) # Inject database session
):
    """
    Retrieve a user by their ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.get(base_path, response_model=list[schemas.UserResponse], tags=["Users"])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of users with pagination.
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users
