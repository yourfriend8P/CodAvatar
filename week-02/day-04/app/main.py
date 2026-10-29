from contextlib import asynccontextmanager
from fastapi import FastAPI, status, HTTPException, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from app.exceptions import TaskNotFoundError
from app.schemas import TaskCreate, TaskUpdate
from app import service
import time

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

@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"completed in {duration:.4f}s"
    )

    response.headers["X-Process-Time"] = f"{duration:.4f}"

    return response

def log_task_created(task_id: int, title: str):
    with open("task_activity.log", "a", encoding="utf-8") as file:
        file.write(f"Created task {task_id}: {title}\n")

@app.get("/")
def home():
    return {"message": "Task Management API is running :)"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/tasks", status_code=201)
def create_task_endpoint(
    task: TaskCreate,
    background_tasks: BackgroundTasks,
):
    created_task = service.create_task(
        title=task.title,
        priority=task.priority,
    )

    background_tasks.add_task(
        log_task_created,
        created_task["id"],
        created_task["title"],
    )

    return created_task


@app.get("/tasks")
def list_tasks():
    return service.get_all_tasks()


@app.get("/tasks/{task_id}")
def get_task_endpoint(task_id: int):
    return service.get_task(task_id)


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

