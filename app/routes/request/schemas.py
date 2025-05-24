
from pydantic import BaseModel




class NewCustomerData(BaseModel):
    first_name: str
    last_name: str
    nationality: str
    gender: str
    birth_date: str

class NewCustomerRequest(BaseModel):
    intention_id: str
    payload: NewCustomerData
    


class NewCustomerIdentificationData(BaseModel):
    document_type: str
    document_number: str
    issued_at: str
    expire_at: str 
    
class NewCustomerIdentificationRequest(BaseModel):
    intention_id: str
    payload: NewCustomerIdentificationData