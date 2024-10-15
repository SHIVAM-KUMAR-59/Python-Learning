# Create a class named 'Programmer' to store information about programmers working at Microsoft.
class Programmer:
    
    # Constructor (__init__) method is used to initialize object attributes for each programmer (name, language, experience).
    def __init__(self, name, language, experience):
        self.name = name                # Name of the programmer
        self.language = language        # Primary programming language of the programmer
        self.experience = experience    # Number of years of experience

    # Instance method 'getInfo' to display the programmer's information.
    def getInfo(self):
        # Prints out a formatted string with the programmer's name, experience, and language.
        print(f"{self.name} has {self.experience} years of experience in {self.language}.")

# Creating instances (objects) of the 'Programmer' class with specific details.
First = Programmer("John Doe", "Python", 3)        
Second = Programmer("Mark Wood", "Javascript", 7)  
Third = Programmer("Stone Cold", "C++", 5)       

# Calling the 'getInfo' method for each programmer to print their information.
First.getInfo()   # Output: John Doe has 3 years of experience in Python.
Second.getInfo()  # Output: Mark Wood has 7 years of experience in Javascript.
Third.getInfo()   # Output: Stone Cold has 5 years of experience in C++.
