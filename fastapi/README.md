# Library Management System (FastAPI + PostgreSQL)

A simple **Library Management System** built with **FastAPI**, **SQLAlchemy**, and **Alembic** — following clean architecture and Domain-Driven Design principles.  
It allows managing **books** and **members**, with operations for **borrowing** and **returning** books, backed by a PostgreSQL database.

---

## Features

-  CRUD operations for **Books** and **Members**
-  Borrow and return book functionality
-  Service Layer (BookService & MemberService)
-  PostgreSQL with SQLAlchemy ORM
-  Database migrations with Alembic
-  Dockerized backend + database
-  Interactive Swagger API docs

---

## Project Structure

#### project/
#### │
#### ├── main.py # FastAPI entry point
#### ├── models/
#### │ ├── book.py # Book model & schema
#### │ └── member.py # Member model & schema
#### ├── services/
#### │ ├── book_service.py # Business logic for books
#### │ └── member_service.py # Business logic for members
#### ├── alembic/ # Alembic migration files
#### │ └── versions/ # Migration history
#### ├── requirements.txt # Python dependencies
#### ├── Dockerfile # Dockerfile for backend
#### ├── docker-compose.yml # Compose file for backend + PostgreSQL
#### └── README.md # Documentation

---

## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/your-username/library-management.git
cd library-management

Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Configure your database

Edit your database URL in main.py (or use .env):

DB_URL = "postgresql+psycopg://postgres:password@localhost:5432/librarydb"

