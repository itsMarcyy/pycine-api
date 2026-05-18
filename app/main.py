from fastapi import FastAPI

from app.database.db import engine, Base
from app.models import media, review
from app.routes.media import router as media_router
from app.routes.review import router as review_router
from app.routes.auth import router as auth_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Pycine",
    description="API for managing movies, TV series and anime with ratings",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Pycine API is running"}


app.include_router(media_router)
app.include_router(review_router)
app.include_router(auth_router)