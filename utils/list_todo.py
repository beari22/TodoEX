import json

from rich.console import Console
from rich.table import Table

console = Console()


def list_todo() -> int:
    """
    shows items in the todo list
    """

    try:
        with open("_todos.json") as todos_file:
            todos = json.loads(todos_file.read())
    except FileNotFoundError:
        console.print(
            "there is no todo file (make a file whit the add command)",
            style="rgb(217,83,79)",
        )
        return 1

    todo_list = Table()
    todo_list.add_column("id", justify="center", no_wrap=True)
    todo_list.add_column("todos", justify="center", no_wrap=True)

    for i in todos:
        if todos[i]["is_done"] == True:
            todo_list.add_row(i, todos[i]["content"], style="rgb(92,184,92)")
        else:
            todo_list.add_row(i, todos[i]["content"])

    console.print(todo_list)

    return 0
