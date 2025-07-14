from fastapi import HTTPException, status
import uuid
from sqlalchemy.orm import Session
from app.models import MyKeys
from app.routes.my_key.schemas import MyKeyConfirm, MyKeyCreate, MyKeyResponse
# --- Service Layer ---


class MyKeysService:
    """
    Service layer to encapsulate business logic for device operations.
    Handles database interactions.
    """

    def create_key(self, db: Session, new_key: MyKeyCreate) -> MyKeys:
        db_device = db.query(MyKeys).filter(
            MyKeys.email == new_key.email).first()

        if db_device:
            db_device.key_value = new_key.key_value
            db_device.user_token = uuid.uuid4()
            db.add(db_device)
            db.commit()
            db.refresh(db_device)
            return db_device
        else:
            new_device = MyKeys(email=new_key.email,
                                key_value=new_key.key_value,
                                user_token=uuid.uuid4())
            db.add(new_device)
            db.commit()
            db.refresh(new_device)
            return new_device

    def verify_key(self, db: Session, confirm_data: MyKeyConfirm) -> bool:
        my_key = db.query(MyKeys).filter(
            MyKeys.user_token == confirm_data.user_token).first()
        
        indexes_keys_array = list(str(confirm_data.indexes))
        match_values_array = list(str(confirm_data.key_value))
        match = True
        if my_key:
            key_value_list = list(str(my_key.key_value))
            for index, val in enumerate(indexes_keys_array):
                if key_value_list[int(val) - 1] != match_values_array[index]:
                    match = False
                    break
            
            return match
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while processing your request"
            )
