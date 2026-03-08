from inventory import Inventory
from prettytable import  PrettyTable
import questionary
import os
inventory = Inventory()
table = PrettyTable()
def start_cli():
    def clean_terminal():
        os.system("cls" if os.name == "nt" else "clear")
    clean_terminal()
    def create_input(text):
        input = questionary.text(
            text,
            qmark=">",
            style=questionary.Style([
                ("qmark","fg:#1d9944 bold"),
                ("instruction", "fg:#314a39 bold"),
                ("answer", "fg:#42e374")
            ])
        ).ask()
        return input
    while True:
        options = {
            "Add product": "add_product",
            "Remove product": "remove_product",
            "Update product": "update_product",
            "List product":  "list_product",
            "Search product": "search_product",
        }
        select = questionary.select(
            "Inventory Manager",
            choices= list(options.keys()),
            instruction=" ",
            use_shortcuts=True,
            style=questionary.Style([
                ("pointer", "fg: #31eb6c bold"),
                ("qmark", "fg:#4cf581 bold"),
                ("highlighted", "fg: #5acc7e bold"),
                # ("question", "fg:#1d9944 bold"),
                ("answer", "fg:#5acc7e")
            ])
        ).ask()
        user_select = options[select]
        if user_select == "add_product":
            while True:
                name = create_input("Enter the product name(Enter 0 to return): ").lower()
                if name == "0":
                    clean_terminal()
                    break
                price = create_input("Enter the product price: ")
                quantity = create_input("Enter the product amount: ")
                result = inventory.add_product(name,price,quantity)
                questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()
                if result[0]:
                    break
        if user_select == "remove_product":
            while True:
                identifier = create_input("Enter the product name or ID(Enter 0 to return): ").lower()
                if identifier == "0":
                    clean_terminal()
                    break
                result = inventory.remove_product(identifier)
                questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()
                if result[0]:
                    break
        if user_select == "update_product":
            while True:
                identifier = create_input("Enter the product name or ID(Enter 0 to return): ").lower()
                if identifier == "0":
                    clean_terminal()
                    break
                price = create_input("Enter the new price: ")
                quantity = create_input("Enter the current amount: ")
                result = inventory.update_product(identifier, price, quantity)
                if result[0]:
                    questionary.print(f"Now, {result[1]}, has the value of {price} and a quantity of {quantity} ", style="bold fg:#1d9944")
                    input("")
                    clean_terminal()
                    break
                questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()
        if user_select == "list_product":
            while True:
                info = inventory.list_items()
                table.add_column("ID", info[0])
                table.add_column("Name", info[1])
                table.add_column("Price", info[2])
                table.add_column("Quantity", info[3])
                print(table)
                input("")
                clean_terminal()
                break
        if user_select == "search_product":
            while True:
                identifier = create_input("Enter the product name or ID(Enter 0 to return): ").lower()
                if identifier == "0":
                    break
                result = inventory.search_product(identifier)
                if result[0]:
                    print(f"* ID: {result[1]}\n* Name: {result[2]["name"].title()}\n* Price: {result[2]["price"]}\n* Quantity: {result[2]["quantity"]}")
                    input("")
                    clean_terminal()
                    break
                questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()

start_cli()