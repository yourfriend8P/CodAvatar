from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import Task


def test_create_task_model():
    engine = create_engine("sqlite:///:memory:")

    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    task = Task(
        title="Learn SQLAlchemy",
        priority=3,
        status="pending",
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    assert task.id is not None
    assert task.title == "Learn SQLAlchemy"
    assert task.priority == 3
    assert task.status == "pending"

    session.close()
    engine.dispose()