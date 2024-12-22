from fastapi import FastAPI
from routers.user import user_router
from routers.Book import book_router
from routers.BorrowRecords import BorrowRecords_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(BorrowRecords_router, prefix="/Borrow", tags=["Borrow"])


@app.get("/")
def home():
    return {"message": "Welcome to bookapp!"}