from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/", response_model=UserResponse)
def home():

    return {
        "id":1,
        "name":"Darshan",
        "password":"12345",
        "email":"abc@gmail.com"
    }