from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.schemas.media import Media, MediaCreate, MediaUpdate
from app.database.db import get_db
from app.models.media import Media as MediaModel


router = APIRouter(
    prefix="/media",
    tags=["Media"]
)


@router.post("/media", response_model=Media) 
def create_media(media: MediaCreate, db: Session = Depends(get_db)):
    db_media = MediaModel(**media.model_dump())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media


@router.get("/media", response_model=list[Media])
def get_medias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)): 
    medias = db.query(MediaModel).offset(skip).limit(limit).all()
    return medias


@router.get("/media/{media_id}", response_model=Media)
def get_media(media_id: int, db: Session = Depends(get_db)):
    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(status_code=404, detail="Media not found")

    return db_media


@router.put("/media/{media_id}", response_model=Media)
def update_media(media_id: int, media: MediaUpdate, db: Session = Depends(get_db)):
    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(status_code=404, detail="Media not found")

    for key, value in media.model_dump().items():
        setattr(db_media, key, value)

    db.commit()
    db.refresh(db_media)
    return db_media


@router.delete("/media/{media_id}", status_code=204)
def delete_media(media_id: int, db: Session = Depends(get_db)):
    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if not db_media:
        raise HTTPException(status_code=404, detail="Media not found")

    db.delete(db_media)
    db.commit()