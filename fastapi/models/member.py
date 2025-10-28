from pydantic import BaseModel
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Member(Base):
    __tablename__ = "members"
    member_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class MemberIn(BaseModel):
    name: str
    email: str

class MemberOut(BaseModel):
    member_id: int
    name: str
    email: str