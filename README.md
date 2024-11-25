# Task Manager Application
This application is a Task Manager implemented in Python, designed to track and manage tasks. It supports both command-line arguments (CLI) for direct task operations and an interactive menu for a user-friendly experience.

## Features

- **Add, update, delete tasks** with ease.
- **Categorize tasks** as `todo`, `in-progress`, or `done`.
- **Persistent storage** using `tasks_tracker.json`.
- Display tasks in a **tabular format**.

## Requirements
- **Python**: Version 3.6 or higher
- **Dependencies**: tabulate (for displaying tasks in tabular format)
- **Install using**: bash
   ```
   pip install tabulate
   ```

### Usage
You can use the application via CLI commands.

Run the script with specific commands to perform operations. Below are the available commands:



## Commands

| Command                        | Description                                  | Example                                       |
|--------------------------------|----------------------------------------------|-----------------------------------------------|
| `add`                          | Add a new task                              | `python3 app.py add "New Task Description"`   |
| `update <task_id> <desc>`      | Update an existing task description          | `python3 app.py update 1 "Updated Task"`     |
| `delete <task_id>`             | Delete a task                               | `python3 app.py delete 1`                    |
| `list`                         | List all tasks                              | `python3 app.py list`                        |
| `mark-in-progress <task_id>`   | Mark a task as "in-progress"                | `python3 app.py mark-in-progress 1`          |
| `mark-done <task_id>`          | Mark a task as "done"                       | `python3 app.py mark-done 1`                 |
| `view-table`                   | View tasks in a tabular format              | `python3 app.py view-table`                  |


## Interactive Menu

Run the application without any arguments to launch the interactive menu:
```bash
python3 app.py
