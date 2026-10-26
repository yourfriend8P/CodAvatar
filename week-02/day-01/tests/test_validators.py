from app.validators import validate_title, validate_priority
import pytest


@pytest.mark.parametrize(
    "title, expected",
    [
        ("Learn Python", "Learn Python"),
        ("  Learn Python  ", "Learn Python"),
    ],
)
def test_validate_title_valid(title, expected):
    assert validate_title(title) == expected


@pytest.mark.parametrize(
    "title",
    [
        "",
        "   ",
    ],
)
def test_validate_title_invalid(title):
    with pytest.raises(ValueError):
        validate_title(title)


@pytest.mark.parametrize(
    "priority",
    [1, 2, 3, 4, 5],
)
def test_validate_priority_valid(priority):
    assert validate_priority(priority) == priority


@pytest.mark.parametrize(
    "priority",
    [0, 6, "3", True],
)
def test_validate_priority_invalid(priority):
    with pytest.raises((ValueError, TypeError)):
        validate_priority(priority)
