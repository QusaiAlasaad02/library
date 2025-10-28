from typing import Optional
from pydantic import BaseModel
from sqlalchemy import String, Integer, Column, Date, Boolean
from sqlalchemy.orm import DeclarativeBase
from datetime import date

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_borrowed = Column(Boolean, nullable=False, default=False)
    borrowed_date = Column(Date, nullable= True, default=None)
    borrowed_by = Column(Integer, nullable=True, default=None)

class BookIn(BaseModel):
    title: str
    author: str

class BookOut(BaseModel):
    book_id: int
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[date] = None
    borrowed_by: Optional[int] = None 