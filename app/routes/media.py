#endpoints para midias

from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from app.schemas.media import Media
from app.schemas.media import MediaCreate
from app.database.db import get_db
from app.database.db import SessionLocal
from app.models.media import Media as MediaModel


router = APIRouter()


@router.post("/media/", response_model=Media)
def create_media(media: MediaCreate, db: Session = Depends(get_db)):
    db_media = MediaModel(**media.dict())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media


@router.get("/media/", response_model=list[Media])
def get_medias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medias = db.query(MediaModel).offset(skip).limit(limit).all()
    return medias


@router.get("/media/{media_id}", response_model=Media) #endpoint para ler uma media específica
def get_media(media_id: int, db: Session = Depends(get_db)):
    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    
    return db_media


@router.delete("/media/{media_id}", status_code=204)
def delete_media(media_id: int, db: Session = Depends(get_db)):
    db_media = db.query(MediaModel).filter(MediaModel.id_ == media_id).first()

    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    
    db.delete(db_media)
    db.commit()