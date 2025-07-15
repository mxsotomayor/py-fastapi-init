from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import MyKeys
from app.routes.my_key.schemas import MyKeyCreate, MyKeyResponse, MyKeyConfirm
from app.routes.my_key.services import MyKeysService

router = APIRouter()

base_path = "/my-keys"


@router.post(base_path, response_model=MyKeyResponse, status_code=status.HTTP_201_CREATED, tags=["My Keys"])
def save_key(new_key: MyKeyCreate, db: Session = Depends(get_db)):
    device_service = MyKeysService()
    try:
        db_device = device_service.create_key(db=db, new_key=new_key)
        return db_device
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {e}"
        )


@router.get(f"{base_path}/has-key", response_model=dict, status_code=status.HTTP_200_OK, tags=["My Keys"])
def validate_key(email: str, db: Session = Depends(get_db)):
    device_service = MyKeysService()
    try:
        myKey: Optional[MyKeys] = device_service.has_key_configured(
            db=db, email=email)
        return {
            "has_key": myKey is not None,
            "user_token": myKey.user_token if myKey is not None else ""
        }
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {e}"
        )


@router.post(f"{base_path}/confirm", response_model=dict, status_code=status.HTTP_200_OK, tags=["My Keys"])
def validate_key(key_confirm: MyKeyConfirm, db: Session = Depends(get_db)):
    device_service = MyKeysService()
    try:
        return {
            "match": device_service.verify_key(db=db, confirm_data=key_confirm)
        }
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {e}"
        )
