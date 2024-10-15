# Class - A class is a blueprint for creating objects. It can contain variables (attributes) and methods (functions).
# Object - An instance of a class that contains its own data and functions.

# Define a class named Employee
class Employee:
    # Class attributes: These are variables that are shared by all instances (objects) of this class.
    name = "Name"  # Default name of the employee
    age = 27       # Default age of the employee
    salary = 25000 # Default salary of the employee

# Creating an object (or instance) of the class Employee.
one = Employee()

# Accessing the 'name', 'age', and 'salary' attributes of the object 'one'.
print(one.name)    # Output: Name
print(one.age)     # Output: 27
print(one.salary)  # Output: 25000

# Object/Instance Attributes - Attributes that are unique to each object, and belong to the instance.
one.height = 5.10  # Setting the 'height' attribute of the object 'one'.
print(one.height)  # Output: 5.10

# Note: Instance attributes have precedence over class attributes during assignment and retrieval when the same attribute name is used.
one.name = "John"  # This will change the 'name' attribute of the object 'one'.
print(one.name)    # Output: John

# Self Parameter - The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# Define a class named Student
class Student:
    name = "John"
    age = 23

    # Static Methods (Decorators) - A class method that does not take self as a parameter.
    @staticmethod
    def greet(): 
        print("Hello")

    # Instance Method - Requires 'self' to access instance-specific data.
    def getInfo(self):  
        print(f"The student's name is {self.name} and their age is {self.age}")

# Creating an object (or instance) of the class Student.
student = Student()

# Calling the static method.
Student.greet()  # Output: Hello

# Calling the instance method. Here, 'self' refers to the 'student' object.
student.getInfo()  # Output: The student's name is John and their age is 23


# Define a class named Car
class Car:

    # Constructor (init method) - The constructor is a special method that is called when an object is created from a class, and it is used to initialize the attributes of the class.
    def __init__(self, name, model, year, color): 
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    # Instance method to display car details
    def getCarDetails(self): 
        print(f"Car name is {self.name}, model is {self.model}, year is {self.year}, and color is {self.color}")

# Creating an instance of the Car class and passing arguments to the constructor.
car = Car("Ford", "Mustang", 1964, "red")

# Calling the method to display car details.
car.getCarDetails()  
# Output: Car name is Ford, model is Mustang, year is 1964, and color is red


# Dunder (Double Underscore) Methods - These are special methods in Python that begin and end with double underscores, often referred to as "magic methods." They are used to customize the behavior of objects in Python.

# __init__ - Initializes a new object (constructor).
# __str__ - Provides a string representation of the object.
# __repr__ - Provides a detailed string representation, mostly used for debugging.

class Book:
    
    # Constructor method (__init__)
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ method provides a user-friendly string representation of the object.
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    # __repr__ method provides a more detailed and technical string representation of the object, useful for debugging.
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

# Creating an instance of the Book class.
book = Book("1984", "George Orwell", 328)

# Printing the book object using __str__.
print(str(book))  # Output: 1984 by George Orwell, 328 pages

# Printing the book object using __repr__.
print(repr(book))  # Output: Book(title='1984', author='George Orwell', pages=328)
