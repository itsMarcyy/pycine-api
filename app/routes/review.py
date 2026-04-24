#endpoints para avaliações
from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from app.schemas.review import Review
from app.schemas.review import ReviewCreate
from app.database.db import get_db
from app.database.db import SessionLocal
from app.models.review import Review as ReviewModel


router = APIRouter()


@router.post("/reviews/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = ReviewModel(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/reviews/", response_model=list[Review])
def get_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviews = db.query(ReviewModel).offset(skip).limit(limit).all()
    return reviews


@router.get("/reviews/{review_id}", response_model=Review) #endpoint para ler uma avaliação específica
def get_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id_ == review_id).first()

    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    
    return db_review


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id_ == review_id).first()

    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    
    db.delete(db_review)
    db.commit()