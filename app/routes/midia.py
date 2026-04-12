#endpoints para midias

from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from app.schemas.midia import Midia
from app.schemas.midia import MidiaCreate
from app.database.db import get_db
from app.database.db import SessionLocal
from app.models.midia import Midia as MidiaModel


router = APIRouter()


@router.post("/midias/", response_model=Midia)
def create_midia(midia: MidiaCreate, db: Session = Depends(get_db)):
    db_midia = MidiaModel(**midia.dict())
    db.add(db_midia)
    db.commit()
    db.refresh(db_midia)
    return db_midia


@router.get("/midias/", response_model=list[Midia])
def get_midias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    midias = db.query(MidiaModel).offset(skip).limit(limit).all()
    return midias


@router.get("/midias/{midia_id}", response_model=Midia) #endpoint para ler uma midia específica
def get_midia(midia_id: int, db: Session = Depends(get_db)):
    db_midia = db.query(MidiaModel).filter(MidiaModel.id_ == midia_id).first()
    if db_midia is None:
        raise HTTPException(status_code=404, detail="Midia not found")
    return db_midia


@router.delete("/midias/{midia_id}", status_code=204)
def delete_midia(midia_id: int, db: Session = Depends(get_db)):
    db_midia = db.query(MidiaModel).filter(MidiaModel.id_ == midia_id).first()

    if db_midia is None:
        raise HTTPException(status_code=404, detail="Midia not found")
    
    db.delete(db_midia)
    db.commit()
