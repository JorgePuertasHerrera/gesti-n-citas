from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from app.db.database import Base

class Categories (Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    specialty = Column(String, index = True)
    description = Column (String)
    doctor_id = Column (Integer, ForeignKey("users.id"))

