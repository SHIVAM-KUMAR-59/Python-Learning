
# Multi - Level Inheritence - A class inherits from another class, which in turn inherits from another class.
"""
Syntax:
class BaseClass:
    # Base class code
    # code

class DerivedClass1(BaseClass):
    # Derived class inheriting from BaseClass
    # code

class DerivedClass2(DerivedClass1):
    # Another class inheriting from DerivedClass1 (multi-level inheritance)
    # code
"""

# Base class (parent class)
class Employee:
    name = "Random"
    def show(self):
        print(f"My name is {self.name}")

# Derived class (inherits from Employee class)
class Programmer(Employee):
    language = "Python"
    def showLanguage(self):
        print(f"{self.name} is good in {self.language} language.")

# Another derived class (inherits from Programmer class)
class Coder(Programmer):
    salary = 12000
    def printLanguage(self):
        print(f"{self.name} codes in {self.language} language and has a salary of {self.salary}")

# Creating an instance of the Coder class
a = Coder()

# Accessing methods from all levels of the inheritance chain
a.show()             # Output: My name is Random (inherited from Employee class)
a.showLanguage()     # Output: Random is good in Python language. (inherited from Programmer class)
a.printLanguage()    # Output: Random codes in Python language and has a salary of 12000 (method in Coder class)
