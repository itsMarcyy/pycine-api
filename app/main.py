from fastapi import FastAPI


from app.database.db import engine, Base
from app.models import midia
from app.models import evaluation


Base.metadata.create_all(bind=engine)

from app.routes.midia import router as midia_router


app = FastAPI(
    title="Pycine",
    description="API para gerenciamento de filmes, séries e animes com avaliações",
    version="1.0.0"
)

app.include_router(midia_router)