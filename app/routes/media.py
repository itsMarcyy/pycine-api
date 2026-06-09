from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.schemas.media import Media, MediaCreate, MediaRating, MediaUpdate
from app.database.db import get_db
from app.models.media import Media as MediaModel
from app.models.user import User
from app.services.auth import get_current_user
from app.models.review import Review as ReviewModel


router = APIRouter(
    prefix="/media",
    tags=["Media"]
)


@router.post(
        "", 
        response_model=Media, 
        summary="Create a new media"
        )

def create_media(
    media: MediaCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
    ):

    db_media = MediaModel(**media.model_dump(), user_id=current_user.id_)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media


@router.get(
        "", 
        response_model=list[Media], 
        summary="Get all media")

def get_medias(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
    ):

    media = db.query(MediaModel).filter(MediaModel.user_id == current_user.id_)
    return media


@router.get(
        "/{media_id}", 
        response_model=Media, 
        summary="Get a media by ID")

def get_media(
    media_id: int, 
    db: Session = Depends(get_db)
    ):

    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(status_code=404, detail="Media not found")

    return db_media


@router.put(
        "/{media_id}", 
        response_model=Media, 
        summary="Update a media")

def update_media(
    media_id: int, 
    media: MediaUpdate, 
    db: Session = Depends(get_db)
    ):

    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(status_code=404, detail="Media not found")

    for key, value in media.model_dump().items():
        setattr(db_media, key, value)

    db.commit()
    db.refresh(db_media)
    return db_media


@router.delete(
        "/{media_id}", 
        status_code=204, 
        summary="Delete a media")

def delete_media(
    media_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):

    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(
            status_code=404, 
            detail="Media not found"
            )
    
    if db_media.user_id != current_user.id_:
        raise HTTPException(
            status_code=403, 
            detail="Not authorized to delete this media"
            )

    db.delete(db_media)
    db.commit()


@router.get(
        "/{media_id}/rating", 
        response_model=MediaRating, 
        summary="Get the rating of a media", 
        description="Returns the average rating of a media.")

def get_media_rating(
    media_id: int, 
    db: Session = Depends(get_db)
    ):

    average_rating = db.query(func.avg(ReviewModel.rating)).filter(ReviewModel.media_id == media_id).scalar()

    if average_rating is None:
        raise HTTPException(status_code=404, detail="Media not found or no reviews available")
    
    return {"media_id": media_id, "average_rating": round(float(average_rating), 1)} # Arredondar para 1 casa decimal
