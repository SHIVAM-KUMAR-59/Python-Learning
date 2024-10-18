from typing import List, Tuple

# Type Definition - Define the type of a variable at the time of declaration
n: int = 5  # 'n' is an integer variable
name: str = "Random"  # 'name' is a string variable

# Function Definition - Define the type of parameters and return type for a function
def sum(a: int, b: int) -> int:  # Function 'sum' takes two integers and returns an integer
    return a + b

# Calling the function 'sum' with correct arguments
# This will work because we are passing two integers to the function
result = sum(n, n)
print(f"Sum of {n} and {n} is: {result}")

# Defining a list of integers using type hinting
a: List[int] = [1, 2, 3, 4, 5]
print(f"List of integers: {a}")

# Defining a tuple of strings using type hinting
b: Tuple[str, ...] = ("a", "b", "c")  # 'Tuple[str, ...]' indicates a tuple with any number of strings
print(f"Tuple of strings: {b}")

# Defining a tuple with a combination of string and integer using type hinting
person: Tuple[str, int] = ("John", 25)
print(f"Person's details: Name = {person[0]}, Age = {person[1]}")
