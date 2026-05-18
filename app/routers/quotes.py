from fastapi import APIRouter, Depends, HTTPException
from app.schemas.quotes import QuoteCreate, QuoteResponse
from app.models.quotes import  Quotes
from app.db.database import get_db
from typing import List

router = APIRouter()

@router.post("/quotes", response_model=QuoteResponse)
def create_quotes( quotes: QuoteCreate, db = Depends(get_db)):
    existing_quotes = db.query(Quotes).filter(Quotes.description == quotes.description).first()
    if existing_quotes:
        raise HTTPException(status_code= 400 , detail= "Quote already exist")
    
    db_quote = Quotes(
       description= quotes.description,
       status = quotes.status,
       datetime= quotes.datetime,
       doctor_id= quotes.doctor_id, 
       center_id= quotes.center_id, 
       patient_id= quotes.patient_id

    )
    
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    
    return db_quote

@router.get("/quotes",response_model=List[QuoteResponse])
def get_quotes(db = Depends(get_db)):
  quotes = db.query(Quotes).all()
  return quotes

@router.put ("/quotes/{id}")
def update_quotes(id: int, quotes: QuoteCreate, db = Depends(get_db)):
    db_quote = db.query(Quotes).filter(Quotes.id == id ).first()
    if db_quote is None:
        raise HTTPException(status_code= 404, detail="Quote not found")
    db_quote.description = quotes.description
    db_quote.status = quotes.status 
    
    db.commit()
    db.refresh(db_quote)
    return db_quote

@router.delete("/quotes/{id}")
def delete_quotes(id: int, db = Depends(get_db)):
    db_quote = db.query(Quotes).filter(Quotes.id == id). first()
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    

    db.delete(db_quote)
    db.commit()
    
    return db_quote
        
        
    
        
        