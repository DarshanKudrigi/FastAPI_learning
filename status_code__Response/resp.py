# # JSONResponse
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# @app.get("/")
# def home():

#     return JSONResponse(
#         status_code=200,
#         content={
#             "message":"Welcome",
#             "success":True
#         }
#     )


# HTMLResponse
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.get("/html")
# def html():

#     return HTMLResponse("""

#         <h1>Hello FastAPI</h1>

#     """)


# PlainTextResponse
# from fastapi import FastAPI
# from fastapi.responses import PlainTextResponse

# app = FastAPI()

# @app.get("/text")
# def text():

#     return PlainTextResponse("Welcome to FastAPI")


# # RedirectResponse


# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# app = FastAPI()

# @app.get("/")
# def home():

#     return RedirectResponse("/docs")



from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def numbers():
    for i in range(1, 6):
        yield(f"{i}\n")

@app.get("/stream")
def stream():
    return StreamingResponse(numbers(), media_type="text/plain")