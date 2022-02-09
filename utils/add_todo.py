import json

from time import sleep
from rich.console import Console

console = Console()


def add_todo(content: str) -> int:
    """
    adds a item the todo list
    """

    try:
        with open("_todos.json") as todos_file:
            todos = json.loads(todos_file.read())
    except FileNotFoundError:
        console.print("file dos not exit, makeing a new file", style="rgb(240,173,78)")
        with open("_todos.json", "w") as todos_file:
            todos_file.write("{}")
            todos = {}

    try:
        new_todo_num = int(list(todos)[-1]) + 1
    except IndexError:
        new_todo_num = 1

    todos[str(new_todo_num)] = {"content": content, "is_done": False}

    with open("_todos.json", "w") as todos_file:
        new_todos = json.dumps(todos, indent=4)
        todos_file.write(new_todos)

    sleep(0.4)

    return 0
