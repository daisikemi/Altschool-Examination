from schemas.books import BookCreate, Books, Book, BookUpdate, PartialUpdate
from fastapi import HTTPException
from typing import Optional


books = [
    Book(id=1, title= "Oops", author="Rotimi Akanni", is_available=True),
    Book(id=2, title= "learning python", author="Kemi Daisi", is_available=True),
    Book(id=3, title= "figuring life", author="Ope Bowale", is_available=True),
]


class BookCrud:

    @staticmethod
    def get_book(book_id):
        user: Optional[Book]=None
        for current_book in books:
            if current_book.id == book_id:
                user = current_book
                break
            return user 


    @staticmethod
    def get_books():
        return books

    
    @staticmethod
    def create_book(book_data: BookCreate):
        book_id = len(Books)+1
        book =Book(id=book_id, **book_data.model_dump())
        Books[book_id] =book
        return book
    
    @staticmethod
    def get_book_by_id(book_id: int):
        book = Books.get(book_id)
        if not book:
            raise HTTPException(status_code=400, detail= "book not found")
        return book
    

    @staticmethod
    def update_book(Book: Optional[Book], data: BookUpdate, user_id : int):
        if not Book:
            raise HTTPException(
                status_code=404, detail="Book not found"
            )
        Book.title = data.title
        Book.author = data.author 
        return Book
    
    
    @staticmethod
    def partially_update_book(book_id, new_data: PartialUpdate):
        book: Book = Books.get(book_id)
        if not Book:
            raise HTTPException(status=404, detail="Book not found.")
        for k, v in new_data.model_dump(exclude_unset=True).items():
            setattr(Book, k, v)
        return book


    @staticmethod
    def delete_book(book_id: int):
        book = BookCrud.get_book(book_id)
        if not book:
            raise HTTPException(status=404, detail="Book not found.")
        books.remove(book)
        return {"message": "Book deleted"}
    
    
    @staticmethod
    def book_unavailable(book_id: int):
        if book not in books:
         raise HTTPException(
            status_code=404, detail="Book not found"
        )
        book = Books [book_id]
        book["is_available"]=False
        return book
    
    
    
book_crud = BookCrud()



