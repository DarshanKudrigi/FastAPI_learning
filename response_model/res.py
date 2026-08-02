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



# 1. What is a Response Model?

# Answer: A response model defines the structure of the data an API returns. It validates the output, filters extra fields, and ensures a consistent response format.
# ✅ Data validation
# ✅ Removes unwanted fields
# ✅ Hides passwords and sensitive data


# 2. What happens if the returned data doesn't match the response model?

# Answer: FastAPI validates the response. If required fields are missing or have incorrect types, it raises a validation error instead of returning invalid data.




# "A response model in FastAPI is a Pydantic model that defines the structure of the API's output. It validates the response, removes unwanted or sensitive fields such as passwords, ensures a consistent JSON format, and helps generate accurate API documentation automatically."



# BaseModel:: is used to define the schema (the shape of the data).


# response_model:: tells FastAPI which schema to use when formatting and validating the API response.