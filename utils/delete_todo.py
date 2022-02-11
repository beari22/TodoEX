import json

from rich.console import Console
from rich.table import Table

console = Console()


def delete_todo(todo_id: str | int) -> int:

    todo_id = str(todo_id)

    try:
        with open("_todos.json") as todos_file:
            todos = json.loads(todos_file.read())
    except FileNotFoundError:
        console.print(
            "there is no todo file (make a file whit the add command)",
            style="rgb(217,83,79)",
        )
        return 1

    one_item_todo_list = Table()
    one_item_todo_list.add_row(todo_id, todos[todo_id]["content"])

    try:
        del todos[todo_id]
    except KeyError:
        console.print("todo dos not exist", style="rgb(217,83,79)")
        return 1

    with open("_todos.json", "w") as todos_file:
        new_todos = json.dumps(todos, indent=4)
        todos_file.write(new_todos)

    console.print(one_item_todo_list, style="red")

    return 0