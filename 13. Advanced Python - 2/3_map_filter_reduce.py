# Map Function - It applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).
# The map object can be converted to a list or any other iterable if needed.

def square(x):
    return x * x

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() to apply the 'square' function to each item in the list 'numbers'
squared_numbers = list(map(square, numbers))

# Print statement showing the original list and the squared result
print(f"Original numbers: {numbers}")
print(f"Squared numbers using map(): {squared_numbers}")  # Output: Squared numbers: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 


# Filter Function - It applies a function to each item in an iterable and returns only the items where the function returns True.
# For example, filtering only even numbers from the list.

# Using filter() to get even numbers from the list 'numbers'
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print statement showing the original list and the filtered even numbers
print(f"Original numbers: {numbers}")
print(f"Even numbers using filter(): {even_numbers}")  # Output: Even numbers: [2, 4, 6, 8, 10]


# Reduce Function - It applies a rolling computation (a function) to the items of an iterable, i.e., it applies the function cumulatively to the items.
# In Python 3.x, reduce() is not a built-in function and needs to be imported from the functools module.

from functools import reduce

# Using reduce() to sum up all the numbers in the list 'numbers'
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Print statement showing the sum of all numbers in the list
print(f"Sum of all numbers using reduce(): {sum_of_numbers}")  # Output: Sum of all numbers: 55
