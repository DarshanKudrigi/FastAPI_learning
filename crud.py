from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI();


todos=[];

class Todo(BaseModel):
    id:int;
    title:str;
    completed:bool;

@app.post("/crete_CRUD")
def crete_CRUD(user:Todo):
    return {
        "message":"hi",
        "user":Todo
    }