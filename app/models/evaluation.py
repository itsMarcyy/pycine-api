from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


from app.database.db import Base


class Evaluation(Base):
    __tablename__ = "avaliacoes"

    id_ = Column(Integer, primary_key=True, index=True)
    midia_id = Column(Integer, ForeignKey("midias.id_"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String)

    midia = relationship("Midia", back_populates="evaluations")