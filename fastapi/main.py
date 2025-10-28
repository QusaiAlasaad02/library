from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

from services.book_service import BookService
from services.member_service import MemberService

from models.book import BookOut, BookIn
from models.member import MemberOut, MemberIn


DB_URL = "postgresql+psycopg://postgres:password@db:5432/librarydb"
engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

@app.post("/books/", response_model=BookOut)
def create_book(payload: BookIn, db: Session = Depends(get_db)):
    svc = BookService(db)
    return svc.create(**payload.model_dump(include={"title", "author"}))

@app.get("/books/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    svc = BookService(db)
    return svc.list()

@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    svc = BookService(db)
    obj = svc.get(book_id)
    if not obj:
        raise HTTPException(404, "Book not found")
    return obj

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, payload: BookIn, db: Session = Depends(get_db)):
    svc = BookService(db)
    obj = svc.update(book_id, **payload.model_dump())
    if not obj:
        raise HTTPException(404, "Book not found")
    return obj

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    svc = BookService(db)
    ok = svc.delete(book_id)
    if not ok:
        raise HTTPException(404, "Book not found")
    return None

@app.post("/books/{book_id}/{member_id}", response_model=BookOut)
def borrow_book(book_id: int, member_id: int, db: Session = Depends(get_db)):
    svc = BookService(db)
    obj = svc.get(book_id)
    if not obj:
        raise HTTPException(404, "Book not found")
    msvc = MemberService(db)
    if not msvc.get(member_id):
        raise HTTPException(404, "Member not found")
    if obj.is_borrowed:
        raise HTTPException(status_code=409, detail="Book is already borrowed")
    return svc.borrow(book_id, member_id)

@app.post("/return/{book_id}", response_model=BookOut)
def return_book(book_id: int, db: Session = Depends(get_db)):
    svc = BookService(db)
    obj = svc.return_back(book_id)
    if not obj:
        raise HTTPException(404, "Book not found")
    return obj



#-------------- Members -----------

@app.post("/members/", response_model=MemberOut, status_code=status.HTTP_201_CREATED)
def create_member(payload: MemberIn, db: Session = Depends(get_db)):
    ms = MemberService(db)
    add = ms.create(**payload.model_dump())

    if not add:
        raise HTTPException(404, "Enter a valid Email")
    
    return add

@app.get("/members/", response_model=list[MemberOut])
def list_members(db: Session = Depends(get_db)):
    ms = MemberService(db)
    return ms.list()

@app.get("/members/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    ms = MemberService(db)
    obj = ms.get(member_id)
    if not obj:
        raise HTTPException(404, "Member not found")
    return obj

@app.put("/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, payload: MemberIn, db: Session = Depends(get_db)):
    ms = MemberService(db)
    obj = ms.update(member_id, **payload.model_dump())
    if not obj:
        raise HTTPException(404, "Member not found")
    return obj

@app.delete("/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    ms = MemberService(db)
    ok = ms.delete(member_id)
    if not ok:
        raise HTTPException(404, "Member not found")
    return None