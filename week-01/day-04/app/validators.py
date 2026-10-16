def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")

    if not title:
        raise ValueError("Title cannot be empty")

    title = title.strip()
    return title


def validate_priority(priority: int) -> int:
    if not isinstance(priority, int):
        raise ValueError("Priority must be an integer")

    if priority < 1 or priority > 5:
        raise ValueError("Priority must be between 1 and 5")

    return priority
