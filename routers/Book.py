from fastapi import APIRouter
from schemas.books import Books, BookCreate, BookUpdate, PartialUpdate, Book
from crud.Book import  book_crud
from typing import Optional


book_router = APIRouter()


@book_router.get("/", status_code=200)
async def get_all_books():
    return {"message": "success", "data": book_crud.get_books()}
    

@book_router.post("/", status_code=201)
async def create_book(book_data: BookCreate):
    book= book_crud.create_book(book_data)
    return {"data": book, "message": "Book created successfully"}

@book_router.get("/user_id", status_code=200)
async def get_book_by_id(book_id : int):
    book = book_crud.get_book_by_id(book_id)
    return {"data": book, "message": "Book created successfully"}

@book_router.put("/{book_id}", status_code=200)
async def update_book(book_id: int, payload: BookUpdate):
    book: Optional[Book] = book_crud.get_book(book_id)
    updated_book: Book = book_crud.update_book(book, book_id, payload)
    return {"message": "Book updated successfully", "data": updated_book}

@book_router.patch("/{book_id}")
async def update_book_partially(book_id: int, payload: PartialUpdate):
    partially_updated_book : Book= book_crud.partially_update_book(book_id, payload)
    return{"message": "success", "data": partially_updated_book}

@book_router.delete("/{book_id}", status_code=200)
def delete_book(book_id: int):
    book_crud.delete_book(book_id)
    return{"message": "Book deleted successfully"}

@book_router.put("/{book_id}")
async def mark_book_unavailable(book_id: int):
    book_unavailable: Book= book_crud.book_unavailable(book_id)
    return{"message": "success", "data": book_unavailable}




