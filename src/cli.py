from inventory import Inventory
import questionary
import os
inventory = Inventory()
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
                name = create_input("Enter the product name(Enter 0 to return): ")
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
                identifier = create_input("Enter the product name or ID(Enter 0 to return): ")
                if identifier == "0":
                    clean_terminal()
                    break
                result = inventory.remove_product(identifier)
                questionary.print(f"* {result[1]}", style="bold fg:#1d9944")
                input("")
                clean_terminal()
                if result[0]:
                    break
start_cli()