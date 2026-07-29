from fastapi import FastAPI
from numpy import number

app = FastAPI();

darshan = "Hello, FastAPI!";
suman = 42;

@app.get("/")
def home():
    return {"darshan": darshan,
            "ragu": suman};

@app.get("/about/{user_id}")
def about(user_id: int):
    return {"message": "This is my first FastAPI application.", "user_id": user_id};

