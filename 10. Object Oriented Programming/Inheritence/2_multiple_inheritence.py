# Multiple Inheritence - A class can inherit from multiple parent classes.

"""
Syntax:
class ChildClass(ParentClass1, ParentClass2):
    Write your commands
"""


# Defining a class named Employee.
class Employee:
    company = "ITC"
    name = "Default name"
    salary = 100000
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}.")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages this is the best {self.language}.")

class Programmer(Employee, Coder): # Programmer class inherits from Employee class and Coder class
    company = "Microsoft"
    def showLanguage(self):
        print(f"{self.company} is good in {self.language} language.")

programmer = Programmer()
programmer.show()
programmer.showLanguage()
programmer.printLanguage()

