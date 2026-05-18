from pydantic import BaseModel, ConfigDict

class CategoriesCreate(BaseModel):
    specialty: str
    description: str
    doctor_id: int 
    
class CategoriesResponse(BaseModel):
      model_config = ConfigDict(from_attributes = True)
      id: int 
      speciality: str
       
        