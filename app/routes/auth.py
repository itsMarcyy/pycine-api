from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.services.auth import create_access_token, get_current_user, get_hash_password, verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Confirmando se o email ja esta registrado
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(
            status_code=401, 
            detail="Invalid email or password"
            )
    
    if not verify_password(
        form_data.password, 
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401, 
            detail="Invalid email or password"
            )
    
    acess_token = create_access_token(data={"sub": str(db_user.id_)})
    
    return {
        "access_token": acess_token, 
        "token_type": "bearer"}


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user