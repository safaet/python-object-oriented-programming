class Dog:
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
		
class Poodle(Dog):
 
    def __init__(self, name, age, code):
        super().__init__(name, age)
        self.code = code


# This line:
#super().__init__(name, ager)

# Is equivalent to the syntax that you learned:

#Dog.__init__(self, name, age)