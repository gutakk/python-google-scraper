from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
import models.user


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String, nullable=False)
    keywords = Column(Integer, nullable=False)
    created = Column(DateTime, server_default=func.now())