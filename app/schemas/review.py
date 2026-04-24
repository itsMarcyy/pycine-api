from typing import List, Optional
from pydantic import BaseModel, Field


#Está dando erro, preciso resolver depois
class Review(BaseModel):
    id_: int
    media_id: int
    rating: float = Field(..., ge=1, le=5)  # Avaliação de 1 a 5, aceitando números decimais como 4.5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    media_id: int
    rating: int  # Avaliação de 1 a 5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia


class ReviewUpdate(BaseModel):
    media_id: Optional[int] = None
    rating: Optional[int] = None  # Avaliação de 1 a 5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia


