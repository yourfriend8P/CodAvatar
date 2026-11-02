import sqlite3

from app.database import create_tables, get_connection


def test_database_connection():
    create_tables()

    connection = get_connection()

    assert isinstance(connection, sqlite3.Connection)

    connection.close()


def test_tasks_table_exists():
    create_tables()

    connection = get_connection()

    result = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name = 'tasks'
    """)

    table = result.fetchone()

    assert table is not None
    assert table["name"] == "tasks"

    connection.close()