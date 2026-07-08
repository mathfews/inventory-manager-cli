from inventory import Inventory
from prettytable import  PrettyTable
import questionary
import os
inventory = Inventory()
table = PrettyTable()
def start_cli(inventory):
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
            table = PrettyTable()
            while True:
                table.field_names = ["ID", "Name", "Price($)", "Amount"]
                rows = inventory.list_items()
                for row in rows:
                    table.add_row([row[0], row[1].title(), f"${row[2]}", int(row[3])])
                print(table)
                input("")
                clean_terminal()
                break
        if user_select == "search_product":
            while True:
                identifier = create_input("Enter the product name or ID(Enter 0 to return): ").lower()
                if identifier == "0":
                    clean_terminal()
                    break
                result = inventory.search_product(identifier)
                if result[0]:
                    table = PrettyTable()
                    table.field_names = ["ID", "Name", "Price($)", "Amount"]
                    table.add_row([result[1][0], result[1][1].title(), f"${result[1][2]}", int(result[1][3])])
                    print(table)
                else:
                    questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()
