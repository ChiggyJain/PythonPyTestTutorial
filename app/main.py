from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}