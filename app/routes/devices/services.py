from sqlalchemy.orm import Session
from app.models import Device
from app.routes.devices.schemas import DeviceCreate, DeviceResponse
# --- Service Layer ---
class DeviceService:
    """
    Service layer to encapsulate business logic for device operations.
    Handles database interactions.
    """
    def create_device(self, db: Session, device: DeviceCreate) -> Device:
        """
        Saves a new device's email and Firebase token to the database.
        If a device with the given email already exists, it updates the token.
        """
        # Check if a device with this email already exists
        db_device = db.query(Device).filter(Device.email == device.email).first()

        if db_device:
            # If device exists, update its fbase_token
            db_device.fbase_token = device.fbase_token
            # date_updated will be automatically updated by onupdate=func.now()
            db.add(db_device)
            db.commit()
            db.refresh(db_device)
            return db_device
        else:
            # If device does not exist, create a new one
            new_device = Device(email=device.email, fbase_token=device.fbase_token)
            # date_created and date_updated will be automatically set by default=func.now()
            db.add(new_device)
            db.commit()
            db.refresh(new_device)
            return new_device
