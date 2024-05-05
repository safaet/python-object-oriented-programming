class Programmer(object):
    
    salary = 100000
    monthly_bonus = 500
    
    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages= programming_languages
 
class Engineer(object):
    
    salary = 100000
    monthly_bonus = 500
    
    def __init__(self, name, age, address, phone, bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.bilingual = bilingual

# Yes! There is a lot of code repetition.

# Both classes have the attributes name, age, address, phone, salary, and monthly_bonus.

# salary and monthly_bonus even have the same value.

# "Do not repeat yourself" is a key principle of software development, so there must be a way to fix this, right?

# Inheritance is the key for avoiding all this repetition.



# 💡 Tip: This is a brief and general introduction to illustrate the importance of inheritance. We will dive into the specific details of this topic and the code in this section and in the next section.



# Conceptually, these two classes are categories (types) of employees.

# So we could create an Employee class with all the attributes and methods that both classes share and make them inherit these attributes and methods from their parent class.

# Let me illustrate this:

# Parent Class
class Employee:

    salary = 100000
    monthly_bonus = 500

    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

# Inherits from Employee
class Programmer(Employee):
    def __init__(self, name, age, address, phone, programming_languages):
        Employee.__init__(self, name, age, address, phone)
        self.programming_languages = programming_languages

# Inherits from Employee
class Assistant(Employee):
    def __init__(self, name, age, address, phone, bilingual):
        Employee.__init__(self, name, age, address, phone)
        self.bilingual = bilingual


programmer = Programmer("Isabel", 45, "5th avenue", "556-345-543", ["Java"])
assistant = Assistant("Jack", 18, "6th avenue", "452-355-234", True)

# Instance attributes
print(programmer.name)
print(assistant.age)

# Class attribute
print(programmer.salary)
print(assistant.monthly_bonus)