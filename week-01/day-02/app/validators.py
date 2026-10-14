def validate_title(title: str) -> str:
    if not isinstance(title, str):
        return "Title must be a string"

    if not title:
        return "Title cannot be empty"

    title = title.strip()
    return "Accepted"


def validate_priority(priority: int) -> int:
    if not isinstance(priority, int):
        return "Priority must be an integer"

    if priority < 1 or priority > 5:
        return "Priority must be between 1 and 5"

    return "Accepted"
