class CashRegister:
    
    TAXES_DECIMAL = 0.05
    def __init__(self, cashier):
        self.cashier = cashier
        self.products = {}        
    
    def add_product(self, new_product, quantity=1):
        self.products[new_product["name"]] = {
            "price": new_product["price"],
            "quantity": quantity
        }
    
    def show_products(self):
        print(self.products)
    
    def remove_product(self, product):
        self.products.pop(product)
    
    def update_price(self, product, new_price):
        self.products[product]["price"] = new_price

    def find_subtotal(self):
        subtotal = 0
        for product_info in self.products.values():
            subtotal += product_info["price"] * product_info["quantity"]
        return subtotal
    
    def print_subtotal(self):
        print(self.find_subtotal())

    def find_taxes(self):
        return round(self.find_subtotal() * CashRegister.TAXES_DECIMAL, 2)
    
    def print_taxes(self):
        print(f"Taxes: {self.find_taxes()}")

    def find_total(self):
        return round(self.find_subtotal() + self.find_taxes(), 2)

    def print_total(self):
        print(f"Total: {self.find_total()}")

    def clear_purchase(self):
        self.products.clear()
    


my_cash_register = CashRegister("Safaet")

product_1 = {"name": "Pizza", "price": 3.54}
product_2 = {"name": "Chocolate", "price": 6.32}
product_3 = {"name": "Pasta", "price": 2.31}

my_cash_register.add_product(product_1)
my_cash_register.add_product(product_2)
my_cash_register.add_product(product_3)

my_cash_register.show_products()

my_cash_register.remove_product("Pizza")
my_cash_register.show_products()

my_cash_register.update_price("Pasta", 5.67)
my_cash_register.show_products()

my_cash_register.print_subtotal()
my_cash_register.print_taxes()
my_cash_register.print_total()

my_cash_register.clear_purchase()
my_cash_register.show_products()