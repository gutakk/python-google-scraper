from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from database import Base
import models.file


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey("file.id"), nullable=False)
    keyword = Column(String, nullable=False)
    total_adword = Column(Integer)
    total_link = Column(Integer)
    total_search_result = Column(String)
    html_code = Column(String)
    created = Column(DateTime, server_default=func.now())
    __table_args__ = (UniqueConstraint('file_id', 'keyword'),)