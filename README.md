This is a simple Library Management System built using FastAPI. It provides endpoints to manage books and borrow records, including adding, returning, and managing availability of books.

Features

Book Management: Add and manage book details, including availability.
Borrow Records: Track borrowed books, including borrow and return dates.
Return Book: Mark a borrowed book as returned, updating its availability and return date.
Installation
Clone the repository: git clone https://github.com/daisikemi/Altschool-Examination.git
cd Altschool-Examination.
Create a virtual environment and activate it: python -m venv venv, source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies: pip install -r requirements.txt
Run the application: uvicorn main:app --reload
Access the app at http://127.0.0.1:8000.
API Endpoints
1. Create a New Book
Endpoint: POST /create-book/
Description: Create a new book and add to the library.
Request Body:
{
  "title": "Book Title",
  "author": "Author Name"
}
Response:

{
  "message": "Book created successfully",
  "book_id": 1
}
2. Get All Books
Endpoint: GET /books/
Description: Retrieves all books in the library.
Response:

[
  {
    "book_id": 1,
    "title": "mouse and cat",
    "author": "Kemi Daisi",
    "is_available": true
  }
]
3. Borrow a Book
Endpoint: POST /borrow-book/
Description: Marks a book as borrowed.
Request Body:

{
  "book_id": 1,
  "borrower": "User 1"
}
Response:

{
  "message": "Book borrowed successfully",
  "borrow_date": "2024-11-21"
}
4. Return a Book
Endpoint: POST /return-borrowed-book/
Description: Marks a borrowed book as returned.
Request Body:

{
  "book_id": 1
}
Response:

{
  "message": "Book 'cat and rat' has been marked as returned",
  "return_date": "2024-12-20"
}
File Structure

fastapi-library-app/
├── main.py            # Main application file
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
