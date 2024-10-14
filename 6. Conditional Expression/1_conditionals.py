# Conditional Statements - Conditional statements in Python allow you to execute different blocks of code based on certain conditions. These statements control the flow of a program, enabling it to make decisions and take actions accordingly.

# Note: Indentation ( White spaces ) are very important in python syntax

# Types of Conditional Statements:

# 1. if-else
"""
Syntax:
if (condition):
    Write your commands for true condition
else:
    Write your commands for false condition
"""

age = int(input("Enter your age: "))
if(age >= 18):
    print("You can vote")
else:
    print("You cannot vote")

print("End of if-else")

# 2. elif also called if-elif-else ladder
"""
Syntax:
if (condition):
    Write your commands for primary true condition
elif (condition):
    Write your commands for secondary true condition
else:
    Write your commands for false condition, when none of the above conditions satisfy
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a > b):
    print("a is greater")
elif(a == b):
    print("a and b are equal")
else:
    print("b is greater")

print("End of if-elif-else ladder")

# 3. Nested if
"""
Syntax:
if (condition):
    if (condition):
        Write your commands for true condition
    else:
        Write your commands for false condition
else:
    Write your commands for false condition
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a > b):
    if(a == b):
        print("a and b are equal")
    else:
        print("a is greater")
else:
    print("b is greater")

print("End of nested if")
