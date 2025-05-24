from app.routes.request.schemas import NewCustomerIdentificationRequest, NewCustomerRequest
from fastapi import Depends, Response, Request
from fastapi import APIRouter
from app.db import get_db
from app.routes.request.services import RequestsService

base_path = "/requests"

router = APIRouter()


@router.get(f"{base_path}/status", tags=["Demo route"])
def get_status(request: Request, db=Depends(get_db)):
    
    intention_id = request.cookies.get("gentoo_intention_id")
    if not intention_id:
        return {"message": "No intention ID found in cookies."}
    
    service = RequestsService(db)
    intention = service.get_intention(intention_id)
    
    if not intention:
        return {"message": "Intention not found."}
    
    return {
        "intention_id": intention.id,
        "status": intention.status,
        "current_step": intention.current_step,
        "created_at": intention.created_at.isoformat(),
    } 


@router.post(f"{base_path}/init", tags=["Demo route"])
def init_intention(response: Response, db=Depends(get_db)):
    service = RequestsService(db)
    id = service.create_intention()
    response.set_cookie(key="gentoo_intention_id", value=str(id), httponly=True)
    return {"intention_id": str(id)}


@router.post(f"{base_path}/1", tags=["Demo route"])
def create_customer(body: NewCustomerRequest, db=Depends(get_db)):
    service = RequestsService(db)
    return service.create_customer(body)


@router.post(f"{base_path}/2", tags=["Demo route"])
def create_customer(body: NewCustomerIdentificationRequest, db=Depends(get_db)):
    service = RequestsService(db)
    return service.create_contact(body)