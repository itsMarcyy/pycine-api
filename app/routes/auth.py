from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register():
    return {"message": "Router is working!"}


@router.post("/login")
def login():
    return {"message": "Router is working!"}

