task: list[dict] = []
next_task_id: int = 1

def create_task(title: str, priority: int) -> dict:
    global next_task_id

    task = {
        "id": next_task_id,
        "title": title,
        "priority": priority,
        "status": "pending",
    }
    task.append(task)
    next_task_id += 1

    return task

def get_all_tasks() -> list[dict]:
    return task

def get_task_by_id(id: int) -> dict:
    for task in task:
        if task["id"] == id:
            return task
    return None

def update_task(id: int, title: str, priority: int) -> dict | None:
    task = get_task_by_id(id)
    if task is None:
        return None
    
    task["title"] = title
    task["priority"] = priority
    return task

def delete_task(id: int) -> bool:
    task = get_task_by_id(id)
    if task is None:
        return False
    task.remove(task)
    return True