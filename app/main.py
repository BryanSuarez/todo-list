from fastapi import FastAPI
from app.api import categories

app = FastAPI(
    title="Todo App",
    description="A simple Todo application with category management.",
    version="0.1.0",
)

# Include routers
app.include_router(categories.router)


# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Todo App"}
