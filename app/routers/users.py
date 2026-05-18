from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.models.user import User
from app.db.database import get_db
from app.utils.security import hash_password
from typing import List 

router = APIRouter()



@router.post ("/users", response_model=UserResponse)
def create_user(user: UserCreate, db = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail = "Email ya registrado")
    
    db_user = User(
        name= user.name,
        email= user.email,
        password= hash_password(user.password) 
    )    
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.get("/users", response_model= List[UserResponse])
def get_users(db = Depends(get_db)):
    users = db.query(User).all()
    return users 

@router.put("/users/{id}")
def update_user(id: int, user: UserCreate, db = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail= "Usuario not found")
    db_user.name = user.name,
    db_user.email = user.email,
    db_user.password = user.password
    
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.delete("/user/{id}")
def delete_user(id:int, db = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user is None:
        raise HTTPException (status_code=404, detail= "User not found")
        
    db.commit()
    db.delete(db_user)
    
    return db_user