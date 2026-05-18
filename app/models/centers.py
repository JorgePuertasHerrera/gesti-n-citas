from sqlalchemy import Column, String, Boolean, Integer
from app.db.database import Base

class Center(Base):
    __tablename__ = "centers"
    id = Column(Integer, primary_key=True, index= True)
    adress = Column(String, index = True)
    city =  Column(String, index = True)
    phone_number = Column(Integer, unique= True, index= True) 
    name = Column(String, unique=True, index= True)
    
    
    