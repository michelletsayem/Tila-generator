import random
from time import sleep
from ui.ui import banner_text
from rich.console import Console
from scripts.scripts import get_file
from ui.ui import clear_scr, display, display_del_db, display_generate_db_menu, exit_program


console = Console()


def main():

    # for fancy purposes
    with console.status("[bold green]Starting Tila generator please wait...") as status:
        sleep(random.choice([2, 6, 3, 3, 4, 2, 3, 5, 1]))

    # main Loop
    while True:
        clear_scr()  # clears screen
        print(banner_text)
        display(consl=console, filenm=get_file("Main-menu-screen.md"))
        choice = input("\n\n\n>>> ")

        if choice == str(1):
            clear_scr()  # clears screen
            display_generate_db_menu(console)
        elif choice == str(2):
            clear_scr()  # clears screen
            display_del_db(console)
        elif choice == str(3):
            clear_scr()  # clears screen
            exit_program(console)
