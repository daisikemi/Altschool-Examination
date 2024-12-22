from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    author: str
    title: str
    is_available: bool = True

class Book(BookBase):
    id: int


class BookCreate(BookBase):
    pass 

class BookUpdate(BookBase):
    pass

class PartialUpdate(BookBase):
    author:Optional [str]
    title: Optional [str]
    is_available: bool = True






Books: dict[int:Book] = {}