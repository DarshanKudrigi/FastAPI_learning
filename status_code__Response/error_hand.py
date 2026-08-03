from fastapi import FastAPI,status
from fastapi import HTTPException

app = FastAPI()

users = {
    1:"Darshan",
    2:"Rahul"
}

@app.get("/user/{id}")
def get_user(id:int):

    if id not in users:
        raise HTTPException(
            # status_code=status.HTTP_401_UNAUTHORIZED,
            status_code=404,
            detail="User Not Found"
        )
    return {
        "name":users[id]
    }



# 1. What is an HTTP status code?

# Answer:
# An HTTP status code is a three-digit code returned by the server that indicates whether a request was successful or if an error occurred.












# Client

#    │

# GET /students/5

#    │

# Server

#    │

# ID exists?

#  ┌───────┐
#  │       │
# Yes      No
#  │        │
#  │        │
# Return    HTTPException
# Student      404

#  │        │

# 200      404