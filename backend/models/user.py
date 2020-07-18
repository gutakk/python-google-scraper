from database import Base
from sqlalchemy import Column, Index, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    __table_args__ = (Index('email_password_idx', 'email', 'password'),)
