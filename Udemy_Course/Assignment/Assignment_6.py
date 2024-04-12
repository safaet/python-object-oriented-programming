#With Decorator
class BouncyBall:
 
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand
    @property
    def price(self,price):
        return self.price
    @price.setter
    def price(self,value):
        if value > 0 and isinstance(value,int):
            self._price = value
        else:
            print ("Please enter valid value ")
    @property
    def size(self):
        return self.size
    @size.setter
    def size(self,value):
        if value > 1 and value < 100:
            self._size = value
        else:
            print("please give size with range 1 to 100")
    @property
    def brand(self):
        return self.brand
    @brand.setter
    def brand(self,value):
        if isinstance(value,str):
            self._brand = value
        else:
            print ("Please write the brand in alphabets.")
        
        
#With Property     
class BouncyBall:
    
    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand
    
    def get_price(self,price):
        return self._price
    
    def set_price(self,value):
        if value > 0 and isinstance(value,int):
            self._price = value
        else:
            print ("Please enter valid value ")
    price = property(get_price, set_price) #property function used
    def get_size(self):
        return self._size
    
    def set_size(self,value):
        if value > 1 and value < 100:
            self._size = value
        else:
            print("please give size with range 1 to 100")
    size = property(get_size, set_size)
    def get_brand(self):
        return self._brand
    
    def set_brand(self,value):
        if isinstance(value,str):
            self._brand = value
        else:
            print ("Please write the brand in alphabets.")
    brand = property(get_brand, set_brand)


