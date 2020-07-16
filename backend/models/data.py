from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
import models.file


class Data(Base):
    __tablename__ = "data"
    file_id = Column(Integer, ForeignKey("file.id"), primary_key=True)
    keyword = Column(String, primary_key=True)
    total_adword = Column(Integer)
    total_link = Column(Integer)
    total_search_result = Column(String)
    html_code = Column(String)
    created = Column(DateTime, server_default=func.now())