from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
def root():
    return {"message": "Home page"}

@app.get("/ping/", status_code=200)
def ping():
    return {"message": "pong"}

