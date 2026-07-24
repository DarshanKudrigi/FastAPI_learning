from fastapi import FastAPI
from numpy import number

app = FastAPI();


#dynamic routes


@app.get("/square/{number}")
def square(number:int):
    return {"square": float(number) ** 2}



#/////////////////////////////////////////////////////////////////////////
# optional parameter

@app.get("/user")
def get_user(name: str = None):
    return {"user_name": name};

#output:{"user_name":"mohit"}

#/////////////////////////////////////////////////////////////////////////


#default_Parameter


@app.get("/product")
def get_product(limit: int = 100):
    return {"product_limit": limit,
            "message":"hello"};


#/////////////////////////////////////////////////////////////////////////


