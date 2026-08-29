from fastapi import FastAPI, Depends

app = FastAPI()

def get_current_user():
    return {
        "id": 101,
        "name": "Darshan"
    }

@app.get("/profile")
def get_profile(user = Depends(get_current_user)):
    return user