

from ast import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Role, User
from app.routes.users import schemas
from app.routes.users.services import RoleService, UserService
from app.routes.users.schemas import UserResponse


router = APIRouter()

base_path = "/users"


@router.post(base_path, response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)  # Inject database session
):
    """
    Create a new user.
    Checks if a user with the given email already exists.
    """
    service = UserService()
    role_service = RoleService()
    db_user = service.get_user_by_email(db, email=user.email)

    roles_to_assign: List[Role] = []
    provided_role_ids = user.role_ids

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    if provided_role_ids:
        fetched_roles = role_service.get_roles_by_ids(db, provided_role_ids)
        if len(fetched_roles) != len(set(provided_role_ids)):
            invalid_ids = set(provided_role_ids) - \
                {role.id for role in fetched_roles}
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"One or more provided role IDs are invalid: {list(invalid_ids)}"
            )
        roles_to_assign.extend(fetched_roles)
    else:
        # Default to 'user' role if no role_ids are provided
        default_user_role = role_service.get_role_by_name(db, "user")
        if not default_user_role:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Default 'user' role not found. Please ensure default roles are created."
            )
        roles_to_assign.append(default_user_role)

    # Create the user using the service layer
    new_user = service.create_user(db=db, user=user, roles=roles_to_assign)
    return new_user


@router.get(f"{base_path}/{{user_id}}", response_model=schemas.UserResponse, tags=["Users"])
def read_user(
    user_id: int,
    db: Session = Depends(get_db)  # Inject database session
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
