from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Confirm, Prompt
from rich.traceback import install as install_traceback

console = Console()

from myutils import *

install_traceback()


#
# TODO (ha, ironic):
#   add sounds and add animations(?)
#



def main():
    console.print(Markdown("# TODO"), justify="center", style="#585858")

    while True:
        try:
            output = Prompt.ask(">> ")
        except KeyboardInterrupt:
            console.print("exiting", style="#d9534f")
            exit()

        match output:
            case "exit":
                console.print("exiting", style="rgb(217,83,79)")
                exit()
            case "add":
                add_todo(Prompt.ask("(content) -> "))
            case "ls" | "list":
                list_todo()
            case "cm" | "done":
                done_todo(Prompt.ask("(todo number) -> "))
                console.print(Markdown("# TODO"), justify="center", style="#585858")
            case "help":
                todo_help()
            case "‌":
                console.print("yes", style="i")
            case "del" | "delete" | "rm" | "remove":
                delete_todo(Prompt.ask("(todo number) -> "))
            case "delall" | "deleteall":
                if Confirm.ask("do you want to delete [b]ALL[/b] the todos") == True:
                    delete_all_todos()
                else:
                    console.print("ok")
            case "cls" | "clear":
                    console.clear()
                    console.print(Markdown("# TODO"), justify="center", style="#585858")



            

if __name__ == "__main__":
    main()
