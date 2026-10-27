from app.validators import validate_title, validate_priority


def create_task(task_data: dict) -> dict:
    if not isinstance(task_data, dict):
        raise TypeError("Task data must be a dictionary")

    # task_data["title"] = validate_title(task_data["title"])
    # task_data["priority"] = validate_priority(task_data["priority"])

    title = validate_title(task_data.get("title"))
    priority = validate_priority(task_data.get("priority"))

    return {
        "id": 1,
        "title": title,
        "priority": priority,
        "status": "pending",
    }
