from fastapi import FastAPI

# Import database components
from app.database import engine, Base

# Import models so Base knows about them
from app.models import category  # Adjust if you have more models

from app.api import categories

# Create database tables
# Note: For production, consider using Alembic for migrations
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo App",
    description="A simple Todo application with category management using MySQL.",
    version="0.1.0",
)

# Include routers
app.include_router(categories.router)


# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Todo App with MySQL backend"}
