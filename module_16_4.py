from fastapi import FastAPI, Path, HTTPException, status, Body
from typing import Annotated, List
from pydantic import BaseModel

#uvicorn module_16_4:app --reload

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
def create_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
        for user in users:
           if user.id == user_id:
              users.remove(user)
              return user
        raise HTTPException(status_code=404, detail="User not found")