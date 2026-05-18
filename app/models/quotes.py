from sqlalchemy import Column, String, Boolean, Integer, DateTime,ForeignKey
from app.db.database import Base

class Quotes (Base):
    __tablename__ = "quotes"
    
    id = Column (Integer, primary_key= True, index= True, unique=True)
    description = Column(String, index = True)
    datetime = Column (DateTime, unique=True, index=True)
    doctor_id = Column (Integer,ForeignKey("users.id"))
    status = Column (Boolean, index= True)
    center_id = Column (Integer, ForeignKey("centers.id"))
    patient_id = Column (Integer, ForeignKey("users.id"))
    