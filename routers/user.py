from typing import Optional
from fastapi import APIRouter
from crud.users import  user_crud
from schemas.users import (
    User,
    UserCreate,
    UserUpdate,
    PartialUpdate
)

user_router = APIRouter()


@user_router.get("/", status_code=200)
async def get_all_users():
    return {"message": "success", "data": user_crud.get_users()}

@user_router.post("/", status_code=201)
async def create_user(user_data: UserCreate):
    user= user_crud.create_user(user_data)
    return {"data": user, "message": "User created successfully"}

@user_router.get("/user_id", status_code=200)
async def get_user_by_id(user_id : int):
    user = user_crud.get_user_by_id(user_id)
    return {"data": user, "message": "Successful"}

@user_router.put("/{user_id}", status_code=200)
async def update_user(user_id: int, payload: UserUpdate):
    user: Optional[User] = user_crud.get_user(user_id)
    updated_user: User = user_crud.update_user(user, user_id, payload)
    return {"message": "successful", "data": updated_user}

@user_router.patch("/{user_id}")
async def update_user_partially(user_id: int, payload: PartialUpdate):
    partially_updated_user : User= user_crud.partially_update_user(user_id, payload)
    return{"message": "successful", "data": partially_updated_user}

@user_router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int):
    return user_crud.delete_user(user_id)

@user_router.put("/{user_id}", status_code=200)
async def deactivate_user(user_id:int):
    deactivated_user : User= user_crud.deactivate_user(user_id,)
    return{"message":"success", "data":deactivated_user}
    


