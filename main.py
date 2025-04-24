from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# create a GET endpoint to list tasks
@app.get("/tasks")
async def list_tasks():
    return {"message": "Tasks listed"}
