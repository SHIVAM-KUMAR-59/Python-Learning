# Recursion - Recursion is a function that calls itself.

"""
Syntax:
def function_name(argument 1, argument 2, argument 3.. argument n):
    if (Base Condition):
        Write your commands
    else:
        Recursive call ( Call the same function with different parameter )
"""

# 1. Function to find the factorial of a number using recursion
def factorial(n):
    # Base condition: if n is 0, return 1 (since 0! = 1)
    if (n == 0 or n == 1):
        print("Base condition reached: factorial(0) = 1")
        return 1
    else:
        # Recursive call: n * factorial(n - 1)
        print(f"Calculating factorial({n}) = {n} * factorial({n - 1})")
        return n * factorial(n - 1)

# Calling the factorial function and printing the result
result = factorial(5)
print(f"The factorial of 5 is: {result}")  # Expected output: 120

# 2. Function to find the sum of first n natural numbers using recursion
def sum(n):
    # Base condition: if n is 0, return 0
    if (n == 0):
        print("Base condition reached: sum(0) = 0")
        return 0
    else:
        # Recursive call: n + sum(n - 1)
        print(f"Calculating sum({n}) = {n} + sum({n - 1})")
        return n + sum(n - 1)

# Calling the sum function and printing the result
result = sum(5)
print(f"The sum of first 5 natural numbers is: {result}")  # Expected output: 15
