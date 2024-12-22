from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

class User(UserBase):
    id: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class PartialUpdate(UserBase):
    name: Optional [str]
    email:Optional [str]
    is_active: bool = True

Users: dict[int:User] = {}