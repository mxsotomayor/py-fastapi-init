from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Customer, CustomerOnBoardIntention
from app.routes.request.schemas import NewCustomerIdentificationRequest, NewCustomerRequest
from uuid import UUID as UUID4
from fastapi import HTTPException


class RequestsService:

    db: Session

    def __init__(self, db: Session):
        self.db = db

    def create_intention(self) -> UUID4:
        intention = CustomerOnBoardIntention(
            created_at=datetime.now(),
            current_step=1,
            payload={},
            status="pending"
        )
        self.db.add(intention)
        self.db.commit()
        self.db.refresh(intention)
        return intention.id

    def get_intention(self, intention_id: str) -> CustomerOnBoardIntention:
        intention = self.db.query(CustomerOnBoardIntention).filter(
            CustomerOnBoardIntention.id == UUID4(intention_id)
        ).first()
        return intention

    def create_customer(self, body: NewCustomerRequest):

        intention = self.get_intention(body.intention_id)
        
        if not intention:
            raise HTTPException(404, "Intention not found")
        
        data = intention.payload
        
        if not data:
            data = {}
        
        data["customer_data"] = body.payload.model_dump()
        
        
        
        intention.payload = data
        intention.current_step = 2
        intention.status = "in_progress"
        
        self.db.add(intention)
        self.db.commit()
        self.db.refresh(intention)
        
        return intention
    
    def create_contact(self, body: NewCustomerIdentificationRequest):
        intention = self.get_intention(body.intention_id)
        
        if not intention:
            raise HTTPException(404, "Intention not found")
        
        data = intention.payload
        
        if not data:
            data = {}
        
        data["customer_identification_data"] = body.payload.model_dump()
        
        intention.payload = data
        intention.current_step = 3
        intention.status = "in_progress"
        
        self.db.add(intention)
        self.db.commit()    
        self.db.refresh(intention)
        
        return intention

      
