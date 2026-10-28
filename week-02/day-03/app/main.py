from contextlib import asynccontextmanager
from fastapi import FastAPI, status, HTTPException
from app.schemas import TaskCreate, TaskUpdate
from app import service

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

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task: TaskCreate):
    return service.create_task(
        title=task.title,
        priority=task.priority,
    )


@app.get("/tasks")
def list_tasks():
    return service.get_all_tasks()


@app.get("/tasks/{task_id}")
def get_task_endpoint(task_id: int):
    task = service.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, task_data: TaskUpdate):
    task = service.update_task(
        task_id=task_id,
        title=task_data.title,
        priority=task_data.priority,
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(task_id: int):
    deleted = service.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return None