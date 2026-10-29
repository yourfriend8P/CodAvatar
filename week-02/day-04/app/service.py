from app.exceptions import TaskNotFoundError

tasks: list[dict] = []
next_task_id: int = 1

def create_task(title: str, priority: int) -> dict:
    global next_task_id

    task = {
        "id": next_task_id,
        "title": title,
        "priority": priority,
        "status": "pending",
    }
    tasks.append(task)
    next_task_id += 1

    return task

def get_all_tasks() -> list[dict]:
    return tasks

def get_task(task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise TaskNotFoundError(task_id)

def update_task(
    task_id: int,
    title: str,
    priority: int,
) -> dict:
    task = get_task(task_id)
    task["title"] = title
    task["priority"] = priority
    return task

def delete_task(task_id: int) -> bool:
    task = get_task(task_id)
    tasks.remove(task)
    return True