from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):

    start_time = time.time()

    print("Request:", request.method, request.url)

    response = await call_next(request)

    end_time = time.time()

    process_time = end_time - start_time

    print("Processing time:", process_time)

    return response