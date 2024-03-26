class BouncyBall:
 
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
              self.price = price

    price = property(get_price, set_price)

    @property
    def get_price(self):
         return self._price
    @price.setter
    def price(self, new_price):
         if new_price > 0:
              self._price = new_price

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if new_size in ['small', 'medium', 'large']:
              self._size = new_size

    @property
    def size(self):
         return self._size
    
    @size.setter
    def size(self, new_size):
         if new_size in ['small', 'medium', 'large']:
              self._size = new_size
      
    size = property(get_size, set_size)

    def get_brand(self):
         return self._brand
    
    def set_brand(self, brand):
         if isinstance(brand, str) and brand:
            self._brand = brand

    brand = property(get_brand, set_brand)

    @property
    def get_brand(self):
         return self._brand
    
    @brand.setter
    def brand(self, new_brand):
         if isinstance(new_brand, str) and new_brand:
              self._brand = new_brand


