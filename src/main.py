from inventory import Inventory
from cli import start_cli

def main():
    inventory = Inventory()
    start_cli(inventory)
if __name__ == "__main__":
    main()