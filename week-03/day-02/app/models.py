from sqlalchemy import Column, Integer, String

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    priority = Column(Integer, nullable=False)
    status = Column(String(20), default="pending", nullable=False)