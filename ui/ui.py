import sys
import datetime
from os import system
from time import sleep
import scripts.scripts
from rich.table import Table
from datetime import datetime
from rich.columns import Columns
from rich.markdown import Markdown


banner_text = """                           
888888888888 88    88              
    88       ""    88              
    88             88              
    88       88    88  ,adPPYYba,  
    88       88    88  ""     `Y8  
    88       88    88  ,adPPPPP88  
    88       88    88  88,    ,88  
    88       88    88  `"8bbdP"Y8  Generator (V1.1)                 
"""


def clear_scr():
    if sys.platform == "win32":
        system("cls")
    elif sys.platform == "darwin":
        system("clear")
    elif sys.platform == "linux":
        system("clear")


def display(consl, filenm) -> None:
    """Simple function to display markdown files with the help of rich"""
    ##permet d'afficher les fichiers
    with open(filenm) as menu:
        markdown = Markdown(menu.read())
    consl.print(markdown)


def display_generate_db_menu(consl) -> None:
    """A simple function that displays main menu"""

    console = consl

    dt = datetime.now()

    print(banner_text)
    display(consl=console, filenm=scripts.scripts.get_file("Generate-db-menu.md"))
    ans = input("\n\n\n>>>1. ")
    if ans == "":
        db_name = dt.strftime("%a_%d_%m_%Y_%H_%M").lower()
        print("|")
        print("+-> database_name: ", db_name)
    else:
        db_name = ans.lower()
        print("|")
        print("+-> database_name: ", db_name)
    ans = input("\n\n>>>2. ")
    if ans == "":
        entries_num = 999
        print("|")
        print("+-> number of entries: ", entries_num)
    else:
        try:
            entries_num = int(ans)
        except:
            print("Oups an error occured, try inputing only digits and no character or don't input very large numbers...Exiting")
            sleep(5)
            sys.exit(-1)
        print("|")
        print("+-> number of entries: ", entries_num)

    sleep(0.5)
    if display_summary(console, db_name, entries_num):
        scripts.scripts.genrate_all_tables(
            consl=console, dbnm=db_name, entries_nm=entries_num)
    else:
        with console.status("[bold yellow]Canceling...") as _:
            sleep(3)


def display_summary(consl, db_nm, entries_nm) -> bool:
    """A simple function that displays the summary of your newly to be generated db and return a bool as confirmation """

    console = consl
    db_name = db_nm
    entries_num = entries_nm

    with console.status("[bold green]Working on Summary...") as _:
        sleep(2.6)
    clear_scr()
    job_table = Table(show_header=True, header_style="bold magenta")
    employee_table = Table(show_header=True, header_style="bold magenta")
    locations_table = Table(show_header=True, header_style="bold magenta")
    country_table = Table(show_header=True, header_style="bold magenta")
    regions_table = Table(show_header=True, header_style="bold magenta")
    print(banner_text)
    display(consl=console, filenm=scripts.scripts.get_file("summary.md"))
    print("\n\n")
    print("Database: ", db_name)
    print("\n")

    # job table
    job_table.add_column("Job",  width=16)
    job_table.add_row("Job_id(🔑)")
    job_table.add_row("Job_title)")
    job_table.add_row("Min_salary")
    job_table.add_row("Max_salary")
    job_table.add_row("")
    job_table.add_row("")
    job_table.add_row("")
    job_table.add_row("")

    # employee table
    employee_table.add_column("Employee",  width=16)
    employee_table.add_row("employee_id(🔑)")
    employee_table.add_row("location_id(🗝️)")
    employee_table.add_row("job_id(🗝️)")
    employee_table.add_row("first_name")
    employee_table.add_row("last_name")
    employee_table.add_row("email")
    employee_table.add_row("phone_number")
    employee_table.add_row("salary")

    # locations
    locations_table.add_column("Locations", width=16)
    locations_table.add_row("location_id(🔑)")
    locations_table.add_row("country_id(🗝️)")
    locations_table.add_row("street_address")
    locations_table.add_row("postal_code")
    locations_table.add_row("city")
    locations_table.add_row("state_province")

    # countries
    country_table.add_column("Countries", width=16)
    country_table.add_row("country_id(🔑)")
    country_table.add_row("region_id(🗝️)")
    country_table.add_row("country_name")
    country_table.add_row("")
    country_table.add_row("")
    country_table.add_row("")

    # here regions
    regions_table.add_column("Regions", width=16)
    regions_table.add_row("region_id(🔑)")
    regions_table.add_row("region_name")
    regions_table.add_row("")
    regions_table.add_row("")
    regions_table.add_row("")
    regions_table.add_row("")

    console.print(Columns([regions_table, country_table, locations_table]))
    print()
    console.print(Columns([job_table, employee_table,]))
    print()
    print("Number of Entries: ", entries_num)
    print("\n\n")
    print("Do you want to start generating the database? [Yes/yes/Y/y)]: ")
    choice = input(">>> ")
    if choice == "Yes" or choice == "Y" or choice == "y" or choice == "yes":
        return True
    else:
        return False


def init_tables(consl, dbname):
    """A simple function that creats all the tables needed"""

    console = consl

    with console.status("[bold green]creating database please wait...") as _:
        try:
            scripts.scripts.create_db(dbname)
            print("Database " + dbname + " has been created successfully !!")
        except:
            print("An Error occured please try again... Exiting")
            sleep(5)
            sys.exit(-1)
        sleep(1)
    with console.status("[bold green]creating tables please wait...") as _:
        try:
            scripts.scripts.create_tables0(dbname)
            print("Done")
        except:
            print("An unkown error occured...Exiting")
            sleep(5)
            sys.exit(-1)


def display_del_db(consl):## ca ne fonctionne pas ,ca narrive pas a supprimmer ca montre erreur
    """A simple fuction that displays the del db option"""

    console = consl

    print(banner_text)
    display(consl=console, filenm=scripts.scripts.get_file("Delete_db.md"))
    ans = input("\n\n\n>>> ")

    if ans == "":
        print("Nothing was given, going back to main menu")
        sleep(5)
    else:
        try:
            scripts.del_db(ans)
            print(f"db {ans} has  successfully been deleted")
            sleep(3)
        except:
            print("Error occured...returning to main menu")
            sleep(2)


def exit_program(consl) -> None:
    """A simple program that safely exit the program """

    console = consl

    clear_scr()
    print(banner_text)
    display(consl=console, filenm=scripts.scripts.get_file("Exiting.md"))
    sleep(3)
    sys.exit(0)