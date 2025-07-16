from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.routes.devices.schemas import DeviceCreate, DeviceResponse
from app.routes.devices.services import DeviceService

router = APIRouter()

base_path = "/devices"

@router.post(base_path, response_model=DeviceResponse, status_code=status.HTTP_201_CREATED, tags=["Register Devices"])
def save_device( device: DeviceCreate, db: Session = Depends(get_db)):
    device_service = DeviceService()
    try:
        db_device = device_service.create_device(db=db, device=device)
        return db_device
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {e}"
        )
    
    