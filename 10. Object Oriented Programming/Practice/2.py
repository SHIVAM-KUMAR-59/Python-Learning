# Import the math module to use mathematical functions like square root.
import math

# Define a class 'Calculator' that can perform square, cube, and square root calculations.
class Calculator:
    def __init__(self, num):
        # Initialize the number to be used in calculations.
        self.num = num

    # Method to calculate the square of the number.
    def square(self):
        return self.num ** 2  # Using the exponentiation operator (**) for optimization
    
    # Method to calculate the cube of the number.
    def cube(self):
        return self.num ** 3  # Using the exponentiation operator (**) for optimization
    
    # Method to calculate the square root of the number.
    def square_root(self):
        return math.sqrt(self.num)

# Create an instance (object) of the Calculator class with the number 36.
a = Calculator(36)

# Call the methods 
print(f"The square of {a.num} is: {a.square()}")           # Output: The square of 36 is: 1296
print(f"The cube of {a.num} is: {a.cube()}")               # Output: The cube of 36 is: 46656
print(f"The square root of {a.num} is: {a.square_root()}")  # Output: The square root of 36 is: 6.0
