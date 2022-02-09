from rich.console import Console
console = Console()

def todo_help() -> int:
    console.print(
        """    [#5bc0de]exit[/#5bc0de] -> exits the program
    [#5bc0de]add[/#5bc0de] -> adds a todo ( takes in todo content )
    [#5bc0de]ls[/#5bc0de] [#8e44ad](or list)[/#8e44ad] -> lists all the todo also tells if they are done or not
    [#5bc0de]done[/#5bc0de] [#8e44ad](or cm)[/#8e44ad] -> marks the todo as done ( takes in todo id  )
    [#5bc0de]del or delete[/#5bc0de] [#8e44ad](or cls or clear)[/#8e44ad] -> deletes a todo (takes in todo id)
    [#5bc0de]delall[/#5bc0de] [#8e44ad](or deleteall)[/#8e44ad] -> deletes all todos"""
    )

    return 0