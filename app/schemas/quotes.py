from pydantic import BaseModel, ConfigDict
from datetime import datetime

class QuoteCreate(BaseModel):
    description: str
    datetime: datetime
    doctor_id : int 
    status: bool 
    center_id: int 
    patient_id: int 

class QuoteResponse(BaseModel):
     model_config = ConfigDict(from_attributes = True)
     
     id: int 
     status: bool 
     description: str

    
    
    