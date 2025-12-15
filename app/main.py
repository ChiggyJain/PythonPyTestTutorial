from fastapi import FastAPI, Depends
from app.dependencies import get_current_user
from fastapi import FastAPI, BackgroundTasks
from app.background_tasks import send_email

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


@app.post("/notify")
async def notify_user(email: str, background_tasks: BackgroundTasks):
    # here endpoint is registered background-tasks
    # added task in background and it will be run immediately after fastapi returning the response only into the same python process
    background_tasks.add_task(
        send_email,
        to=email,
        subject="Welcome!"
    )
    return {"status": "scheduled"}