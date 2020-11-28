"""
    Luto - A simple, minimal todo list app

    Created by Hoang Tuan

    Version 1.0.0

    This is the source file of it.
"""

from rich.console import Console
from rich.theme import Theme
import random
from os import system

theme = Theme({"cmd": "italic bold", "content": "bold", "error": "bold red"})
cons = Console(theme=theme)
todos = []
FILE = "database.txt"
color_list = ["red", "green", "blue", "yellow", "magenta", "bold white"]
tags = {}
need_to_save = False


# Functions
def save_todos():
    with open(FILE, "w") as fl:
        for todo in todos:
            content, tag = todo
            fl.write(f"{content}: {tag}\n")
        fl.close()


cons.print("Welcome to [red]Luto[/red]!")
cons.print("Type [cmd]help[/cmd] for help")
cons.print("And [cmd]quit[/cmd] to quit")


while True:
    cons.print("Todos:")
    for todo in todos:
        content, tag = todo
        tag_color = tags[tag]
        cons.print(f"   - [content]{content}[/content]: [{tag_color}]{tag}[/{tag_color}]")
    cons.print()
    ipt = cons.input(">>>")
    parts = ipt.split()
    if parts[0] == "help":
        cons.print("""
        Luto version 1.0.0

        [b]Commands[/b]:
            [cmd]add[/cmd]: Add a todos
            [cmd]delete[/cmd]: Delete a todos
            [cmd]help[/cmd]: Display this help
            [cmd]quit[/cmd] or [cmd]exit[/cmd]: Quit the program
            [cmd]save[/cmd]: Save the todo list
            [cmd]delete_all[/cmd]: Delete all the todos
            [cmd]clear[/cmd]: Clear the screen
            
            # [b]Further features:[/b]
                [cmd]delete_tag[/cmd]: Delete every todo that has the same tag
        """)
    elif parts[0] == "delete":
        try:
            todo_to_delete = int(parts[1])
            todos.pop(todo_to_delete)
        except Exception:
            cons.print(f"[error]Error: {Exception}[/error]")
    elif parts[0] == "quit" or parts[0] == "exit":
        if need_to_save is False:
            break
        elif need_to_save is True:
            choice = cons.input("Save?(Y/n) ")
            if choice.lower() == "y":
                save_todos()
                need_to_save = False
                break
            elif choice.lower() == "n":
                break
    elif parts[0] == "clear":
        system("clear")
    elif parts[0] == "add":
        content = cons.input("Enter the content:")
        tag = cons.input("Enter tag name:")
        if tag not in tags:
            color = random.choice(color_list)
            tags[tag] = color
        todos.append((content, tag))
        cons.print("A [i]todo[/i] has been added! :smile:")
        need_to_save = True
    elif parts[0] == "save":
        if need_to_save is False:
            choice = cons.input("Overwrite?(Y/n) ")
            if choice.lower() == "y":
                save_todos()
                need_to_save = False
            elif choice.lower() == "n":
                pass
        elif need_to_save is True:
            save_todos()
            need_to_save = False
    elif parts[0] == "delete_all":
        todos = []
        need_to_save = True
    else:
        cons.print(f"[error]Error: Invalid command: {parts[0]}[/error]")