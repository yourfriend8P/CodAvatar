from fastapi.testclient import TestClient
from app.main import app
from app.service import tasks

client = TestClient(app)


def setup_function():
    tasks.clear()


def test_create_and_list_tasks():
    response = client.post(
        "/tasks",
        json={"title": "Learn CRUD", "priority": 2},
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_update_task():
    created = client.post(
        "/tasks",
        json={"title": "Old title", "priority": 1},
    )

    task_id = created.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "New title", "priority": 4},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "New title"
    assert response.json()["priority"] == 4


def test_delete_task():
    created = client.post(
        "/tasks",
        json={"title": "Temporary task", "priority": 3},
    )

    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 404