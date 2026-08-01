
#path+Query+Body Combo

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI();

users=[];

class User(BaseModel):
    id:int;
    name:str;
    age:int; 


@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message":"created",
        "User":user
    }

@app.put("/users/{user_id}")
def Update_user(user_id:int,user:User,notify:bool):
    if(user_id < len(users) ):
        users[user_id]=user;
        return {
            "Message":"User Updated",
            "notify":notify,
            "Data":user
        }


@app.get("/user")
def get_user():  
    return {"users":users}