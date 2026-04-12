from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/db_pycine"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)
SessionLocal = sessionmaker(bind=engine) #conexão

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()