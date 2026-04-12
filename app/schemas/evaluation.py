from typing import List, Optional
from pydantic import BaseModel


class Evaluation(BaseModel):
    id_: int
    midia_id: int
    rating: int  # Avaliação de 1 a 5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia

    class Config:
        from_attributes = True


class EvaluationCreate(BaseModel):
    midia_id: int
    rating: int  # Avaliação de 1 a 5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia


class EvaluationUpdate(BaseModel):
    midia_id: Optional[int] = None
    rating: Optional[int] = None  # Avaliação de 1 a 5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia