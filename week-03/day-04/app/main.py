from contextlib import asynccontextmanager
from fastapi import FastAPI, status, HTTPException, Request, BackgroundTasks, Depends
from fastapi.responses import JSONResponse
from app.exceptions import TaskNotFoundError
from app.schemas import TaskCreate, TaskUpdate, TaskResponse, UserCreate, UserResponse
from app import service
import time
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application is Starting")

    Base.metadata.create_all(bind=engine)

    yield

    print("Application is Shutting down")


app = FastAPI(
    title="Task Management API",
    description="A learning project from backend development",
    version="1.0.0",
    lifespan=lifespan,
)

# ---- exception handler ----
@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )

# ---- middleware ----
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

# ---------------------- helper functions ----------------------
def log_task_created(task_id: int, title: str):
    with open("task_activity.log", "a", encoding="utf-8") as file:
        file.write(f"Created task {task_id}: {title}\n")

# ---------------------- endpoints ----------------------

# user endpoints 
@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# ---- home endpoint ----
@app.get("/")
def home():
    return {"message": "Task Management API is running :)"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# ---- tasks endpoint ----

#create task endpoint
@app.post(
    "/users/{user_id}/tasks",
    response_model=TaskResponse,
)
def create_task(
    user_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    new_task = models.Task(
        **task.model_dump(),
        user_id=user_id,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

#get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# get task by id
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task

# update task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    updates = task_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

# delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}

