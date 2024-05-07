class Vehicle:
    
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  # In Km/h
        self.fuel_type = fuel_type

# Write your code below:

class Car(Vehicle):
    
    default_speed = 80
    
    def __init__(self,color, fuel_type, num_doors, is_electric, speed=default_speed):
        Vehicle.__init__(self, color , speed, fuel_type)
        self.num_doors = num_doors
        self.is_electric = is_electric
        
        
my_car = Car("Blue", 100, "petrol", 4, True)
print(my_car)