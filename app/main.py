from fastapi import FastAPI


from app.database.db import engine, Base
from app.models import media
from app.models import review
from app.routes.media import router as media_router
from app.routes.review import router as review_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Pycine",
    description="API para gerenciamento de filmes, séries e animes com avaliações",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"msg": "API Pycine funcionando"}

app.include_router(media_router)
app.include_router(review_router)