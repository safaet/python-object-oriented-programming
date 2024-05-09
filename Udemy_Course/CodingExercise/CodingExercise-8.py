class Pizza:
    
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # On a scale from 1 to 5

class Margherita(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        super().__init__(size, toppings, price, rating)
        self.has_extra_cheese = has_extra_cheese

class Marinara(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_oregano):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_oregano = has_extra_oregano

margherita = Margherita("Small", ["Mashroom"], 12, 4, True)
marinara = Marinara("Large", ["Oregano"], 13.8, 4, True)