from fastapi import APIRouter
from schemas.BorrowRecords import BorrowRecordBase, BorrowCreate, ReturnBook
from crud.BorrowRecords import  borrow_crud


BorrowRecords_router = APIRouter()


@BorrowRecords_router.post("/borrow-book", status_code=201)
async def borrow_book(data:BorrowCreate ):
    borrow = borrow_crud.borrow_book(data)
    return {"data":borrow}

@BorrowRecords_router.post("/return-book", status_code=201)
async def return_book(data:ReturnBook):
    returnBook=borrow_crud.return_book(data)
    return returnBook

@BorrowRecords_router.get("/users/{user_id}/borrowing_records", status_code=200)
async def borrow_record(user_id:int):
    records=borrow_crud.get_borrowing_records(user_id)
    return {"data":records}


@BorrowRecords_router.get("/get_all_records", status_code=200)
async def get_all_records():
    return {"message": "success", "data": borrow_crud.get_all_borrowing_records()}
    



