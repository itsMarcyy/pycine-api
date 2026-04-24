# Schemas validam entrada e saída da API.
# Create = entrada | Midia = saída | Update = atualização parcial
# Não confundir com Model (banco de dados)


from typing import List, Optional
from pydantic import BaseModel, field_validator
from enum import Enum
import unicodedata


def normalize_text(text: str) -> str:
    text = text.lower() # Converte para minúsculas
    text = unicodedata.normalize('NFD', text) # Remove acentos
    text = text.encode('ascii', 'ignore').decode('utf-8') # Remove caracteres especiais
    return text


class MediaType(str, Enum):
    movies = "filme"
    series = "serie"


class Media(BaseModel):
    id_: int
    title: str
    description: str
    release_year: int
    genre: str
    type_midia: MediaType

    class Config:
        from_attributes = True  #Permite que o Pydantic leia objetos do SQLAlchemy (não só dict), necessário para retornar dados do banco no response_model


class MediaCreate(BaseModel):
    type_midia: MediaType 

    @field_validator("type_midia", mode="before") #Valida o campo type_midia antes de criar a instância, garantindo que seja normalizado
    @classmethod 
    def normalize_type_midia(cls, value):
        if isinstance(value, str): #isinstance verifica se o valor é uma string, para evitar erros caso já seja do tipo MediaType
            return normalize_text(value) #Chama a função de normalização para garantir que o valor seja consistente, independentemente de como o usuário o forneça (ex: "Filme", "filme", "FILME" serão tratados como "filme")
        return value

    title: str
    description: str
    release_year: int
    genre: str


class MediaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[str] = None
    type_midia: Optional[MediaType] = None  # "filme" ou "serie"