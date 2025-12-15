from fastapi import FastAPI, Depends
from app.dependencies import get_current_user

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}


@app.get("/me")
async def read_current_user(user: dict = Depends(get_current_user)):
    return user