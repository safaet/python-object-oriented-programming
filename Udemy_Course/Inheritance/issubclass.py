class Animal:
    
    def __init__(self, age):
        self.age = age

class Dog(Animal):
    
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.name = name

# The function returns True because Dog is a subclass of Animal.
print(issubclass(Dog, Animal))