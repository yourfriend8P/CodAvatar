def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")

    title = title.strip()

    if len(title) > 100:
        raise ValueError("Title must be less than 100 characters")

    if not title:
        raise ValueError("Title cannot be empty")

    return title


def validate_priority(priority: int) -> int:
    if isinstance(priority, bool) or not isinstance(priority, int):
        raise TypeError("Priority must be an integer")

    if not 1 <= priority <= 5:
        raise ValueError("Priority must be between 1 and 5")

    return priority
