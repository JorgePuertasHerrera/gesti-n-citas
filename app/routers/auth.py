from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserLogin 
from app.db.database import get_db
from app.models.user import User
from app.utils.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db= Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    acces_token = create_access_token(
        data ={"sub": str(db_user.id)}
    )
    
    return {"access_token": acces_token}