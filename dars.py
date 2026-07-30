from fastapi import FastAPI

from pydantic import BaseModel


app=FastAPI();

class User(BaseModel):
    name:str;
    age:int;


@app.post("/User_Model")
def Darshan(user:User):
    return{
            "message":"done",
            "data":user
    }


# @app.post("/items")
# def create_item(user:dict):
#     return {
#         "Message":"created SUCCS",
#         "data":user
#             }