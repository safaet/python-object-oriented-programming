class Professor:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Write your code below:

class ScienceProfessor(Professor):
    
    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        Professor.greet_students(self)
    
    
science_professor = ScienceProfessor("Safaet", 28, "Science")