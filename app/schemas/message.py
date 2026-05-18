from pydantic import BaseModel, ConfigDict 
from datetime import datetime

class MessageCreate(BaseModel):
     contenido: str
     fecha: datetime 
     emisor : int
     receptor: int

class MessageResponse(BaseModel):
     model_config = ConfigDict(from_attributes=True)
     id: int
     fecha: datetime
     contenido: str
     receptor: int
     emisor: int
    