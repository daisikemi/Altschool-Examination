from schemas.users import UserCreate, Users, User, UserUpdate, PartialUpdate
from fastapi import HTTPException
from typing import Optional

users = [
    User(id=1, email="rotimiakanni@gmail.com", name="Rotimi Akanni", is_active=True),
    User(id=2, email="kemidaisi@gmail.com", name="Kemi Daisi", is_active= True),
    User(id=3, email="Opsycul@gmail.com", name="Ope Bowale ", is_active= True),
]


class UserCrud:

    @staticmethod
    def get_user(user_id):
        user: Optional[User]=None
        for current_user in users:
            if current_user.id == user_id:
                user = current_user
                break
            return user 


    @staticmethod
    def get_users():
        return users

    
    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(Users)+1
        user =User(id=user_id, **user_data.model_dump())
        Users[user_id] =user
        return user
    
    @staticmethod
    def get_user_by_id(user_id: int):
        user = Users.get(user_id)
        if not user:
            raise HTTPException(status_code=400, detail= "user not found")
        return user
    

    @staticmethod
    def update_user(User: Optional[User], data: UserUpdate, user_id : int):
        if not User:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        User.name = data.name
        User.email = data.email
        User.name = data.name 
        return User
    
    
    @staticmethod
    def partially_update_user(user_id, new_data: PartialUpdate):
        user: User = Users.get(user_id)
        if not User:
            raise HTTPException(status=404, detail="User not found.")
        for k, v in new_data.model_dump(exclude_unset=True).items():
            setattr(User, k, v)
        return user
    
    @staticmethod
    def delete_user(user_id: int):
        user = UserCrud.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        users.remove(user)
        return {"message": "User deleted"}
    
    @staticmethod
    def deactivate_user(user_id: int):
        if user not in users:
            raise
        HTTPException(status_code=404, detail="User not found")

        user=users[user_id]
        user["is_active"]=False
        return user
    
    
user_crud = UserCrud()



