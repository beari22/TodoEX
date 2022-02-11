import json

from rich.console import Console
from rich.table import Table

console = Console()


def delete_all_todos() -> int:

    try:
        with open("_todos.json") as todos_file:
            todos = json.loads(todos_file.read())
    except FileNotFoundError:
        console.print(
            "there is no todo file (make a file whit the add command)",
            style="rgb(217,83,79)",
        )
        return 1

    if todos == {}:
        console.print("[red]there are no todos in file[/] ( add one by useing 'add' )")
        return 1

    todo_list = Table()

    for i in list(todos):
        todo_list.add_row(i, todos[i]["content"])

    for i in list(todos):
        del todos[i]


    with open("_todos.json", "w") as todos_file:
        new_todos = json.dumps(todos, indent=4)
        todos_file.write(new_todos)

    console.print(todo_list, style="red")

    return 0
