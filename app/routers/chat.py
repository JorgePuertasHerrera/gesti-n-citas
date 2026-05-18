from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.db.database import SessionLocal
from app.schemas.message import MessageCreate,MessageResponse
from app.models.message import Message
from app.db.database import get_db
from datetime import datetime
from typing import List
from fastapi import Depends
router = APIRouter()

# Guarda las conexiones activas
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        
    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)


    async def broadcast(self, message: str):
        for connection in self.active_connections:
         await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/{user_id}/{receptor_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, receptor_id: int, token: str):
    from app.utils.security import get_current_user
    from app.db.database import SessionLocal
    
    db = SessionLocal()
    
    try:
        user = get_current_user(token= token, db=db)
    except:
        await websocket.close(code = 1000)
        return
    finally:
        db.close()    
    
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            
            db = SessionLocal()
            db_message= Message(
                emisor= user_id,
                receptor= receptor_id,
                contenido= data,
                fecha= datetime.now()
            )
            
            db.add(db_message)
            db.commit()
            db.close()
            
            await manager.broadcast(f"Mensaje de {user_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        
@router.get("/messages", response_model = List[MessageResponse])
def get_messages(db= Depends(get_db)):
 return db.query(Message).all()