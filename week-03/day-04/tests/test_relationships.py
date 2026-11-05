from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import User, Task


def test_user_has_multiple_tasks():
    engine = create_engine("sqlite:///:memory:")

    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    user = User(
        username="alex",
        email="alex@example.com",
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    task_one = Task(
        title="Learn Python",
        priority=2,
        user_id=user.id,
    )

    task_two = Task(
        title="Build API",
        priority=3,
        user_id=user.id,
    )

    session.add_all([task_one, task_two])
    session.commit()

    assert len(user.tasks) == 2
    assert user.tasks[0].owner.username == "alex"

    session.close()
    engine.dispose()