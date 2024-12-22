from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: datetime
    return_date: datetime

class Borrow(BorrowRecordBase):
    id: int

class BorrowCreate(BorrowRecordBase):
    user_id: int

class ReturnBook(BorrowRecordBase):
    book_id: int

class BorrowResponse(BaseModel):
    Title: str
    is_available: bool
    borrowed_by: Optional[str]

class BorrowingRecordList(BaseModel):
    records: List[BorrowRecordBase]





BorrowRecord: dict[int:Borrow] = {}
     


