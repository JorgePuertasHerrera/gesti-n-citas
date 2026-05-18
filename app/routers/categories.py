from fastapi import APIRouter, Depends, HTTPException
from app.schemas.categories import CategoriesCreate, CategoriesResponse
from app.models.categories import  Categories
from app.db.database import get_db
from typing import List

router = APIRouter()

@router.post("/categories", response_model=CategoriesResponse)
def create_categories(categories: CategoriesCreate, db = Depends(get_db)):
    existing_files = db.query(Categories).filter(Categories.specialty == categories.specialty).first()
    if existing_files:
        raise HTTPException(status_code=400, detail="Categories already exist")
    db_categories = Categories(
        specialty= categories.specialty,
        description=categories.description,
        doctor_id=categories.doctor_id
    )
    
    db.add(db_categories)
    db.commit()
    db.refresh(db_categories)
    
    return db_categories

@router.get("/categories", response_model=List[CategoriesResponse])
def get_categories(db= Depends(get_db)):
    db_categories = db.query(Categories).all()
    if db_categories is None:
        raise HTTPException(status_code=404, detail="Categories dosn`t exist")
    return db_categories

@router.put("/categories/{id}", response_model=CategoriesResponse)
def put_categories(id: int, categories: CategoriesCreate, db= Depends(get_db)):
    db_categories = db.query(Categories).filter(Categories.id == id).first()
    if db_categories is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    db_categories.specialty = categories.specialty
    db_categories.description= categories.description
    db_categories.doctor_id= categories.doctor_id
    
    db.add(db_categories)
    db.commit()
    db.refresh(db_categories)
    return db_categories

@router.delete("/categories/{id}")
def delete_categories(id: int, db= Depends(get_db)):
    db_categories = db.query(Categories).filter(Categories.id == id).first()
    if db_categories is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    
    db.delete(db_categories)
    db.commit()
    
    return db_categories