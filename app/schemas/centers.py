from pydantic import BaseModel, ConfigDict

class CenterCreate(BaseModel):
    adress: str
    city: str
    phone_number: int
    name: str 

class CenterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    name : str