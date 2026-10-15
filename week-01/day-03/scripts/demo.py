# DEMO for task creation to send demo data and test the results acc to the data sent
from app.task_service import create_task

task_data = {"title": "Learning Python", "priority": 3}

task = create_task(task_data)
if task:
    print("Created task:", task)
    print("Original input:", task_data)
else:
    print("Failed to create task")
