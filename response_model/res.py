from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str

@app.get("/users", response_model=List[User])
def users():

    return [
        {
            "id":1,
            "name":"Ram",
            "password":"123"
        },
        {
            "id":2,
            "name":"Shyam",
            "password":"456"
        }
    ]