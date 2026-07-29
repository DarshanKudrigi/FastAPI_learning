from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI();

class User(BaseModel):
    name:str;
    age:int;
    email:str;


@app.post("/User_Model")
def Darshan(user:User):
    return{
            "message":"done",
            "data":user
    }
