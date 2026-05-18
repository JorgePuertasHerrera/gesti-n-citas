from fastapi import APIRouter, Depends, HTTPException
from app.schemas.centers import CenterCreate, CenterResponse
from app.models.centers import  Center
from app.db.database import get_db
from typing import List

router = APIRouter()

@router.post("/center", response_model= CenterResponse)
def create_center(center: CenterCreate, db= Depends(get_db)):
    existing_center = db.query(Center).filter(Center.name == center.name).first()
    if existing_center:
        raise HTTPException(status_code=400, detail="Center also exist")
    
    db_center = Center(
         adress= center.adress,         
         city= center.city,
         phone_number= center.phone_number,
         name= center.name        
    )
    
    db.add(db_center)
    db.commit()
    db.refresh(db_center)
    
    return db_center

@router.get("/center", response_model=List[CenterResponse])
def get_center(db= Depends(get_db)):
    centers = db.query(Center).all()
    return centers 

@router.put("/center/{id}")
def put_center(id: int, center: CenterCreate, db = Depends(get_db)):
    db_center = db.query(Center).filter(Center.id == id).first()
    if db_center is None:
        raise HTTPException(status_code=400, detail="Center also exist")
    db_center.adress = center.adress
    db_center.city = center.city
    db_center.phone_number = center.phone_number
    db_center.name = center.name 
    
    db.commit()
    db.refresh(db_center)
    
    return db_center

@router.delete("/center/{id}")
def delete_center(id: int, db = Depends(get_db)):
    db_center = db.query(Center).filter(Center.id == id).first()
    if db_center is None:
        raise HTTPException(status_code=404, detail="Center not found")
    
    db.delete(db_center)
    db.commit() 
    
    return db_center   