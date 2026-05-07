from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


def validate_rating(
    value: float,
):  # Validação personalizada para garantir que a nota seja de 0.5 em 0.5
    if (value * 2) % 1 != 0:
        raise ValueError("A nota deve ser de 0.5 em 0.5")
    return value


class Review(BaseModel):
    id_: int
    media_id: int
    rating: float = Field(
        ..., ge=1, le=5
    )  # Avaliação de 1 a 5, aceitando números decimais como 4.5
    comment: Optional[str] = None  # Comentário opcional sobre a mídia

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    media_id: int
    rating: float = Field(..., ge=1, le=5)
    comment: Optional[str] = None  # Comentário opcional sobre a mídia

    @field_validator("rating")  # Validação personalizada para garantir que a nota seja de 0.5 em 0.5
    @classmethod
    def validate_rating(cls, value):
        return validate_rating(value)


class ReviewUpdate(BaseModel):
    media_id: Optional[int] = None
    rating: Optional[float] = Field(None, ge=1, le=5)
    comment: Optional[str] = None  # Comentário opcional sobre a mídia

    @field_validator(
        "rating"
    )  # Validação personalizada para garantir que a nota seja de 0.5 em 0.5
    @classmethod
    def validate_rating(cls, value):
        return validate_rating(value)
