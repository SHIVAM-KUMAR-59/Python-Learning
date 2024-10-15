
# Inheritence - Inheritance in Python is a mechanism where a new class (called a derived class or child class) inherits attributes and methods from an existing class (called a base class or parent class). This allows you to reuse and extend the functionality of the base class without rewriting code.

"""
Syntax:
class ParentClass: 
    def function(self):
        Write your commands

class ChildClass(ParentClass):  # Child class inherits from ParentClass
    def function(self):
        Write your commands 
"""

# Defining a class named Employee.
class Employee:
    company = "ITC"
    name = "Default name"
    salary = 100000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

class Programmer(Employee): # Programmer class inherits from Employee class
    company = "Microsoft"
    def showLanguage(self):
        print(f"{self.company} is good in {self.language} language.")


# Creating an object (or instance) of the class Employee.
one = Employee()

# Creating an object (or instance) of the class Programmer.
two = Programmer()

# Accessing the 'company' attribute of the object 'one'.
print(one.company)  # Output: ITC

# Accessing the 'company' attribute of the object 'two'.
print(two.company)  # Output: Microsoft

# Types of inheritence
# 1. Single Inheritence - A class inherits from a single parent class.