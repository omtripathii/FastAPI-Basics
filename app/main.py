from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register Routes
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Task Manager"}
