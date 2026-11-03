from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn backend development",
            "priority": 3,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Learn backend development"
    assert data["priority"] == 3
    assert data["status"] == "pending"


def test_get_all_tasks():
    client.post(
        "/tasks",
        json={"title": "Task one", "priority": 2},
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_single_task():
    client.post(
        "/tasks",
        json={"title": "Task one", "priority": 2},
    )

    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Task one"


def test_task_not_found():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task 999 not found"


def test_update_task():
    client.post(
        "/tasks",
        json={"title": "Old title", "priority": 1},
    )

    response = client.put(
        "/tasks/1",
        json={"title": "Updated title", "priority": 5},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    assert response.json()["priority"] == 5


def test_delete_task():
    client.post(
        "/tasks",
        json={"title": "Temporary task", "priority": 2},
    )

    response = client.delete("/tasks/1")

    assert response.status_code == 204

    response = client.get("/tasks/1")

    assert response.status_code == 404


def test_invalid_priority():
    response = client.post(
        "/tasks",
        json={"title": "Invalid task", "priority": 10},
    )

    assert response.status_code == 422


def test_blank_title():
    response = client.post(
        "/tasks",
        json={"title": "   ", "priority": 2},
    )

    assert response.status_code == 422