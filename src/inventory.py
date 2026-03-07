import random
class Inventory:
    def __init__(self):
        self.database = {}
        self.next_num = 0
    def exists_or_not(self, name):
        exits = any(item["name"] == name for item in self.database.values())
        return exits
    def generate_id(self):
        self.next_num += 1
        return self.next_num
    def add_product(self, name, price, quantity):
        if self.exists_or_not(name):
            return False, f"The product {name} already exits!"
        try:
            real_name = int(name)
            return False, "The name must be a text!"
        except (ValueError, TypeError):
            pass
        try:
            real_price = float(price)
            if real_price < 0:
                return False, "Enter a positive price!"
        except (ValueError, TypeError):
            return False, "Enter a numeric price!"
        try:
            real_quantity = int(quantity)
            if real_quantity < 0:
                return False, "Enter a positive quantity!"
        except(TypeError, ValueError):
            return False, "Enter a numeric quantity!"
        self.database[self.generate_id()] = {
            "name":  name,
            "price": real_price,
            "quantity": real_quantity
        }
        return True, f"Product {name} succesfully added!"
    def check_name_find_id(self, identifier):
        # why should i switch type() to isinstance() here?
        try:
            real_id = int(identifier)
            if real_id in self.database.keys():
                return True, real_id
            return False, f"Product ID {real_id} not found!"
        except (ValueError, TypeError):
            for item in list(self.database.keys()):
                if identifier == self.database.get(item)["name"]:
                    return True, item
            return False, f"Product {identifier} not found!"
    def list_items(self):
        i = 0
        products_ids = []
        producst_names = []
        products_prices = []
        product_quantites = []
        print("ID | Name | Price | Quantity")
        for products_id, product in self.database.items():
            products_ids.append(products_id)
            producsts_names.append(product["name"])
            products_prices.append(product["price"])
            product_quantites.append(product["quantity"])
        return products_ids, producst_names, products_prices, product_quantites
    def update_product(self, identifier, new_price, quantity):
        product = self.check_name_find_id(identifier)
        if product[0]:
            self.database[product[2]]["price"] = float(new_price)
            return True
        return False
    def remove_product(self, identifier):
        product = self.check_name_find_id(identifier)
        if product[0]:
            name = self.database.get(product[1])["name"]
            del self.database[product[1]]
            return True, f"Product {name} succesfully deleted!"
        return False, f"Product {identifier} not found!"
    def search_product(self, identifier):
        product = self.check_name_find_id(identifier)
        if product[0]:
            info = self.database[product[2]]
            return True, product[2], info
        return False, product[1]