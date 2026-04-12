# Schemas validam entrada e saída da API.
# Create = entrada | Midia = saída | Update = atualização parcial
# Não confundir com Model (banco de dados)


from typing import List, Optional
from pydantic import BaseModel


class Midia(BaseModel):
    id_: int
    title: str
    description: str
    release_year: int
    genre: str
    type_midia: str  # "filme", "série" ou "anime"

    class Config:
        from_attributes = True  #Permite que o Pydantic leia objetos do SQLAlchemy (não só dict), necessário para retornar dados do banco no response_model


class MidiaCreate(BaseModel):
    title: str
    description: str
    release_year: int
    genre: str
    type_midia: str  # "filme", "série" ou "anime"


class MidiaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[str] = None
    type_midia: Optional[str] = None  # "filme", "série" ou "anime"