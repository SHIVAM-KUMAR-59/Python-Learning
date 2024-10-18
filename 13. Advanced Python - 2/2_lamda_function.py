# 'lambda' Keyword - It is used to create anonymous functions in Python.
# Anonymous functions are functions that don't have a name and are typically used for small, throwaway operations.

"""
Syntax:
lambda arguments: expression
"""

# Example 1: Lambda function to calculate the square of a number
square = lambda n: n * n

# Print statement explaining the operation
print(f"The square of 5 is: {square(5)}")  # Output: The square of 5 is: 25

# Example 2: Lambda function to calculate the sum of three numbers
sum = lambda a, b, c: a + b + c

# Print statement explaining the operation
print(f"The sum of 1, 2, and 3 is: {sum(1, 2, 3)}")  # Output: The sum of 1, 2, and 3 is: 6
