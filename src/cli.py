from inventory import Inventory
import questionary
import os
def start_cli():
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
            ("question", "fg:#1d9944 bold"),
            ("answer", "fg:#5acc7e")
        ])
    ).ask()
    return options[select]
print(tart_cli())    def clean_terminal():
        os.system("cls" if os.name == "nt" else "clear")
