from fastapi import HTTPException
from schemas.BorrowRecords import ReturnBook, BorrowRecordBase, BorrowCreate, BorrowRecord, Borrow
from schemas.books import Books
from schemas.users import Users
from crud.users import users
from datetime import datetime


BorrowRecords = [
    {"user_id": 1, "book_id": 1, "borrow_date": "2024-01-10", "return_date": None},
    {"user_id": 1, "book_id": 3, "borrow_date": "2024-01-15", "return_date": None},
]

BorrowingRecords = {
   1:[
    {"book_id": 1, "borrow_date": "2024-01-10", "return_date": "2024-01-25"},
    {"book_id": 3, "borrow_date": "2024-01-15", "return_date": "2024-01-20"},
   ],
   2:[
   {"book_id": 6, "borrow_date": "2024-01-20", "return_date": "2024-01-30"},
   {"book_id": 19, "borrow_date": "2024-01-28", "return_date": "2024-03-30"}
   ]
}


class BorrowCrud:

  @staticmethod
  def borrow_book(borrow_data: BorrowCreate ):
    user = Users.get(borrow_data.user_id)
    book = Books.get(borrow_data.book_id)

    # Check if user exists and is active
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user["is_active"]:
        raise HTTPException(status_code=400, detail="User is not active")
    
    # Check if the book exists and is available
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book["is_available"]:
        raise HTTPException(status_code=400, detail="Book is not available for borrowing")
    
    # Update the book to mark it as borrowed by the user
    book["is_available"] = False
    book["borrowed_by"] = borrow_data.user_id

    # Return the updated book info
    borrow_id = len(BorrowRecord) + 1
    borrow_book = Borrow(
            borrow_id,
            book=borrow_data.book_id,
            **borrow_data.model_dump()
        )
    return borrow_book
    

# Find the borrow record for this user and book
  @staticmethod
  def return_book(data: ReturnBook):
    book_id = data.book_id
   #check if book exist
    if book_id not in BorrowRecords:
        raise HTTPException(status_code=400, detail="Book not found")
    
    book = BorrowRecords[book_id]

    #check if the book is borrowed
    if book["is_available"]:
       raise HTTPException(status_code=400, detail="Book is Available")
    
    # Find the borrow record for the book
    borrow_record = next(
        (record for record in BorrowingRecords.values() if record["book_id"] == book_id and record["return_date"] is None),
        None
    )

    if not borrow_record:
        raise HTTPException(status_code=404, detail="No active borrow record found for this book")

    # Update the borrow record and book status
    borrow_record["return_date"] = datetime.now().strftime("2024-05-11")
    book["is_available"] = True

    return {
        "message": f"Book '{book['title']}' has been marked as returned",
        "return_date": borrow_record["return_date"],
    }
  
# Endpoint to get borrowing records for a specific user
  @staticmethod
  def get_borrowing_records(user_id: int):
    user_record = BorrowingRecords.get(user_id)
    if user_id not in BorrowingRecords:
        raise HTTPException(status_code=404, detail="User not found")
    return user_record
  
  @staticmethod
  def get_all_borrowing_records():
     return BorrowingRecords
     
    
  
  
borrow_crud = BorrowCrud()
 


