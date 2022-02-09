import json

from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

console = Console()



def done_todo(todo_id: str | int) -> int:
    from time import sleep

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

    try:
        if todos[todo_id]["is_done"] == True:
            console.print("that task is already done", style="rgb(92,184,92)")
            return 1
    except KeyError:
        console.print(
            "add a todo that is in the file (use ls to list the todos)",
            style="rgb(217,83,79)",
        )
        return 1

    console.clear()

    one_item_todo_list = Table()
    one_item_todo_list.add_row(todo_id, todos[todo_id]["content"])

    console.print(one_item_todo_list)

    todos[todo_id]["is_done"] = True

    with open("_todos.json", "w") as todos_file:
        new_todos = json.dumps(todos, indent=4)
        todos_file.write(new_todos)

    sleep(1)
    console.clear()

    one_item_todo_list = Table()
    one_item_todo_list.add_row(
        todo_id, todos[todo_id]["content"], style="rgb(92,184,92)"
    )

    console.print(one_item_todo_list)

    sleep(1)
    console.clear()

    console.print(Markdown("# TODO"), justify="center", style="#585858")

    return 0
