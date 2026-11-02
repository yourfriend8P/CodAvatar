import pytest

from app.service import reset_tasks


@pytest.fixture(autouse=True)
def clean_tasks():
    reset_tasks()
    yield
    reset_tasks()