from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from app.schemas import TaskCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application is Starting")

    yield

    print("Application is Shutting down")


app = FastAPI(
    title="Task Management API",
    description="A learning project from backend development",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {"message": "Task Management API is running :)"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def greet(name: str):
    return f"hello {name}"

@app.post("/tasks")
def create_task(task: TaskCreate, status_code=status.HTTP_201_CREATED):
    return {"message": "Task created successfully", "task": task.model_dump()}