# endpoints para avaliações
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


from app.models.user import User
from app.schemas.review import Review, ReviewCreate, ReviewUpdate
from app.database.db import get_db
from app.database.db import SessionLocal
from app.models.review import Review as ReviewModel
from app.services.auth import get_current_user


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/reviews", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_review = ReviewModel(**review.model_dump(), user_id=current_user.id_)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/reviews", response_model=list[Review])
def get_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    reviews = db.query(ReviewModel).filter(ReviewModel.user_id == current_user.id_)
    return reviews


@router.get("/reviews/{review_id}", response_model=Review)
def get_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id_ == review_id).first()

    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    return db_review


@router.put("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id_ == review_id).first()

    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    for key, value in review.model_dump().items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)
    return db_review


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id_ == review_id).first()

    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(db_review)
    db.commit()