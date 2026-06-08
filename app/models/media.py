from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base


class Media(Base):
    __tablename__ = "media"

    id_ = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id_"))
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    description = Column(String, nullable=False)
    release_year = Column(Integer)
    media_type = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="media")
    user = relationship("User", back_populates="media")