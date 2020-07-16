from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String, nullable=False)
    keywords = Column(Integer, nullable=False)
    created = Column(DateTime, server_default=func.now())


class Data(Base):
    __tablename__ = "data"
    file_id = Column(Integer, ForeignKey("file.id"), primary_key=True)
    keyword = Column(String, primary_key=True)
    total_adword = Column(Integer)
    total_link = Column(Integer)
    total_search_result = Column(String)
    html_code = Column(String)
    created = Column(DateTime, server_default=func.now())