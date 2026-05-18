from fastapi import APIRouter


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

