-- Create a table
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status TEXT DEFAULT 'pending'
);

-- Insert records
INSERT INTO tasks (title, priority)
VALUES ('Learn SQL', 2);

INSERT INTO tasks (title, priority)
VALUES ('Build backend API', 4);

-- Retrieve all records
SELECT * FROM tasks;

-- Retrieve one record
SELECT * FROM tasks WHERE id = 1;

-- Filter records
SELECT * FROM tasks WHERE priority >= 3;

-- Update a record
UPDATE tasks
SET status = 'completed'
WHERE id = 1;

-- Delete a record
DELETE FROM tasks WHERE id = 2;