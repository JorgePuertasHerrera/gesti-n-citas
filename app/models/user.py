from sqlalchemy import Column, String, Boolean, Integer
from app.db.database import Base

class User (Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, index = True)
    email = Column(String, unique= True, index = True)
    password = Column(String)
    address = Column(String)
    role = Column(String)