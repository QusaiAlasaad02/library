from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.book import Book  

class BookService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, author: str) -> Book:
        obj = Book(title=title, author=author)
        self.db.add(obj)
        self.db.flush()
        self.db.refresh(obj)
        return obj

    def get(self, book_id: int) -> Optional[Book]:
        return self.db.get(Book, book_id)

    def list(self) -> list[Book]:
        return self.db.execute(select(Book)).scalars().all()

    def update(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None) -> Optional[Book]:
        obj = self.db.get(Book, book_id)
        if not obj:
            return None
        if title is not None: obj.title = title
        if author is not None: obj.author = author
        self.db.flush()
        self.db.refresh(obj)
        return obj

    def delete(self, book_id: int) -> bool:
        obj = self.db.get(Book, book_id)
        if not obj: 
            return False
        self.db.delete(obj)
        return True

    def borrow(self, book_id: int, member_id: int) -> Optional[Book]:
        obj = self.db.get(Book, book_id)
        if not obj: return None
        if obj.is_borrowed: return obj
        obj.is_borrowed = True
        obj.borrowed_date = date.today()
        obj.borrowed_by = member_id
        self.db.flush() 
        self.db.refresh(obj)
        return obj

    def return_back(self, book_id: int) -> Optional[Book]:
        obj = self.db.get(Book, book_id)
        if not obj: return None
        if not obj.is_borrowed: return obj
        obj.is_borrowed = False
        obj.borrowed_date = None
        obj.borrowed_by = None
        self.db.flush(); self.db.refresh(obj)
        return obj
