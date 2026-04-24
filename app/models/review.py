from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base


class Review(Base):
    __tablename__ = "reviews"

    id_ = Column(Integer, primary_key=True, index=True)
    media_id = Column(Integer, ForeignKey("media.id_"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(255))

    media = relationship("Media", back_populates="reviews")