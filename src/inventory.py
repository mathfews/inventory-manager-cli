import random
import sqlite3
class Inventory:
    def __init__(self):
        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "name TEXT NOT NULL UNIQUE," \
        "price REAL CHECK (price > 0)," \
        "amount REAL CHECK (amount >= 0)" \
        "), STRICT")
        self.connect.commit()
    def _handle_integrity_error(self, error, name=None):
        error = str(error)
        if "products.name" in error:
            return False, f"The product {name.capitalize()} already exists!"
        elif "products.price" in error:
            return False, "The price must be a real number!"
        elif "products.amount" in error:
            return False, "The amount must be a real number!"
        elif "price > 0" in error:
            return False, "Prices must be greater than zero"
        elif "amount >= 0" in error:
            return False, "Amounts cannot be negative!"
        return False, "An unexpected database error occurred."
    def add_product(self, name, price, quantity):
        try:
            self.cursor.execute("INSERT INTO products (name, price, amount) VALUES (?,?,?)", (name, price, quantity))
        except sqlite3.IntegrityError as error:
            return self._handle_integrity_error(error, name)
        self.connect.commit()
        self.cursor.execute("SELECT * FROM products")
        return True, f"Product {name.capitalize()} succesfully added!"
    def check_name_find_id(self, identifier):
        try:
            id = int(identifier)
            self.cursor.execute("SELECT id, name, price, amount FROM products WHERE id = ?", (id,))
        except (ValueError, TypeError):
            name = str(identifier).lower()
            self.cursor.execute("SELECT id, name, price, amount FROM products WHERE name = ?", (name,))
        product = self.cursor.fetchone()
        if product:
            return True, product
        else:
            return False, "Product not found!"
    def list_items(self):
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        return rows
    def update_product(self, identifier, new_price, new_quantity):
        product = self.check_name_find_id(identifier)
        if product[0]:
            try:
                self.cursor.execute("UPDATE products SET price = ?, amount = ? WHERE id = ?", (new_price, new_quantity, product[1][0]))
                self.connect.commit()
            except sqlite3.IntegrityError as error:
                return self._handle_integrity_error(error, product[1][1])
            return product
        else:
            return product
    def remove_product(self, identifier):
        product = self.check_name_find_id(identifier)
        if product[0]:
            name = self.database.get(product[1])["name"]
            del self.database[product[1]]
            return True, f"Product {name} succesfully deleted!"
        return False, f"Product {identifier} not found!"
    def search_product(self, identifier):
        product = self.check_name_find_id(identifier)
        return product[0], product[1]
