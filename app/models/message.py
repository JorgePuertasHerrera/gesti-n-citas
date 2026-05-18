from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from app.db.database import Base 

class Message(Base):
    __tablename__= "message"
    
    id= Column (Integer, primary_key = True, index = True)
    emisor= Column(Integer, ForeignKey("users.id"), index = True)
    receptor= Column(Integer, ForeignKey("users.id"), index = True)
    contenido= Column(String, index= True)
    fecha= Column (DateTime, index= True)