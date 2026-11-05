from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import User, Task


def test_create_task_model():
    engine = create_engine("sqlite:///:memory:")

    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    # Create a user first
    user = User(
        username="alex",
        email="alex@example.com",
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    # Create a task belonging to that user
    task = Task(
        title="Learn SQLAlchemy",
        priority=3,
        status="pending",
        user_id=user.id,
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    assert task.id is not None
    assert task.title == "Learn SQLAlchemy"
    assert task.priority == 3
    assert task.status == "pending"
    assert task.user_id == user.id
    assert task.owner.username == "alex"

    session.close()
    engine.dispose()