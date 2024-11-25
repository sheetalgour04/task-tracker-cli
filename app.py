import sys
import json
from datetime import datetime
import tabulate


arguments = []

task_count = 1
tasks = list({})

task_tracker_read = open("tasks_tracker.json", "r")

tasks_read = []

if task_tracker_read.read(1) == "":
    pass
else:
    with open("tasks_tracker.json", "r") as task_tracker_read:
        tasks_read = json.load(task_tracker_read)

for i in range(1, len(sys.argv)):
    arguments.append(sys.argv[i])

tasks = tasks_read


def task_add(arguments=arguments, tasks_in=tasks):
    """Function to add new task"""
    try:
        task_count = tasks[-1]["id"]
    except:
        task_count = 0

    tasks.append(
        {
            "id": task_count + 1,
            "description": arguments[1],
            "status": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    print(f"Task added successfully (ID: {task_count})")
    return tasks_in


def task_update(arguments=arguments, tasks_in=tasks):
    """Function to update the task"""
    for task in tasks_in:
        if task["id"] == int(arguments[1]):
            print(f"Updating the Task from {task['description']} to {arguments[2]}")
            task["description"] = arguments[2]
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Task updated successfully [ID: {arguments[1]}]")
    return tasks_in

    # print(tasks)


def task_delete(arguments=arguments, tasks_in=tasks):
    """Function to delete the task_id mentioned"""
    count = 0
    for task in tasks_in:
        if task["id"] == int(arguments[1]):
            break
        count += 1
    tasks.__delitem__(count)

    print(f"Task deleted successfully (ID: {arguments[1]})")
    return tasks_in


def task_list():
    """Function to list all the tasks present"""
    for task in tasks:
        print(f"{task['id']} : {task['description']}")


def mark_in_progress():
    """Function to mark a task as in-progress"""
    for task in tasks:
        if task["id"] == int(arguments[1]):
            task["status"] = "in-progress"
            print(f"Task ID: {task['id']} marked done")

    return tasks


def mark_done():
    """Function to mark a task as completed"""
    for task in tasks:
        if task["id"] == int(arguments[1]):
            task["status"] = "done"
            print(f"Task ID: {task['id']} marked done")

    return tasks


def list_todo():
    """Function to list all the tasks to do"""
    for task in tasks:
        if task["status"] == "todo":
            print(f"{task['id']} : {task['description']}")


def list_in_progress():
    """Function to list all the tasks which are in progress"""
    for task in tasks:
        if task["status"] == "in-progress":
            print(f"{task['id']} : {task['description']}")


def list_done():
    """Function to list all the tasks which are completed"""
    for task in tasks:
        if task["status"] == "done":
            print(f"{task['id']} : {task['description']}")


def view_table():
    """Function to View all the tasks with creation and modification time"""
    print(
        tabulate.tabulate(
            tasks,
            {
                "headers": [
                    "TASK_ID",
                    "TASK_DESCRIPTION",
                    "TASK_STATUS",
                    "Created at",
                    "Modified at",
                ]
            },
            tablefmt="fancy_grid",
        )
    )


if arguments[0] == "add":
    tasks = task_add()
elif arguments[0] == "update":
    tasks = task_update()
elif arguments[0] == "delete":
    tasks = task_delete()
elif arguments[0] == "list":
    if len(arguments) <= 1:
        task_list()
    else:
        if arguments[1] == "todo":
            list_todo()
        elif arguments[1] == "in-progress":
            list_in_progress()
        elif arguments[1] == "done":
            list_done()
elif arguments[0] == "mark-done":
    tasks = mark_done()
elif arguments[0] == "mark-in-progress":
    tasks = mark_in_progress()
elif arguments[0] == "view-table":
    view_table()
else:
    print(
        """
          Please input the operation - 

          1. add "Task description"
          2. update "Task ID"
          3. delete "Task ID"
          4. list
          5. list done
          6. list todo
          7. list in-progress
          8. mark-done "Task ID"
          9. mark-in-progress "Task ID"
          10. view-table
          """
    )


final_tasks_list = []

for task in tasks:
    final_tasks_list.append(task)


with open("tasks_tracker.json", "w+") as task_tracker_write:
    json.dump(final_tasks_list, task_tracker_write, indent=2)


# task_tracker_write.write(tasks.values())
