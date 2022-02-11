import click

from myutils import *


@click.group()
def main():
    """
    this is a normal'ish todo app
    """
    pass


@main.command("add")
@click.argument("ctx", type=str)
def on_add(ctx):
    add_todo(ctx)

@main.command("done")
@click.argument("ctx", type=int)
def on_done(ctx):
    done_todo(ctx)


@main.command("ls")
def on_list():
    list_todo()

@main.command("del")
@click.argument("ctx", type=int)
def on_delete(ctx):
    delete_todo(ctx)

@main.command("delall")
def on_delete_all():
    delete_all_todos()

@main.command("help")
def on_help():
    todo_help()

if __name__ == "__main__":
    main()
