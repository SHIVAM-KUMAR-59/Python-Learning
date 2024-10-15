# Functions are groups of commands/statements that perform a specific task

"""
Syntax:
Defining/Creating a function:
def function_name(argument 1, argument 2, argument 3.. argument n):
    Write your commands

Calling the function: Whenever we want to call a function, we use the function_name followed by parenthesis
function_name(parameter 1, parameter 2, parameter 3.. parameter n)
"""

# Types of functions:
# 1. Built-in functions - functions provided by Python itself like print(), len(), etc.
# 2. User-defined functions - functions created by the user and written by the user

# 1. Defining a function to greet the user without any arguments
def good_day():
    name = input("Enter your name: ")
    print(f"Have a good day {name}")

# Calling the function
good_day()

# 2. Defining a function to calculate and print the average of three numbers taking the 3 numbers as argument
def average(a, b, c):
    # Calculating the average of the three numbers
    avg = (a + b + c) / 3
    # Printing the result
    print(f"The average of {a}, {b}, and {c} is {avg}")

# Calling the function with different values
print("Calling the function with values 10, 12, 13:")
average(10, 12, 13)  # Expected output: 11.666666666666666

print("\nCalling the function with values 14, 15, 16:")
average(14, 15, 16)  # Expected output: 15.0

# 3. Defining a function to greet and have a default argument
def greet(name, end = "Thank You"): # end = "Thank You" is the default argument
    print(f"Have a good day {name}. {end}") 

# Calling the function
greet("Soham") # Expected output: Have a good day Soham. Thank You, Since no end argument is passed the default value "Thank You" will be used
greet("Soham", "Have a good day") # Expected output: Have a good day Soham. Have a good day, here the end argument is passed as "Have a good day" thus the default value "Thank You" will not be used

# 4. Defining a function to calculate and return the sum of three numbers taking the 3 numbers as argument
def sum(a, b, c):
    # Calculating the sum of the three numbers
    total = a + b + c
    # Returning the result
    return total

# Calling the function with different values
print("Calling the function with values 10, 12, 13:")
sum1 = sum(10, 12,13) # Calling the function and storing the returned value in a variable
print(sum1)  # Expected output: 33

print("\nCalling the function with values 14, 15, 16:")
print(sum(14, 15, 16))  # Expected output: 54

