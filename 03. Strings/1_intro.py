# There are 3 ways to create a string
# Strings are immutable in python

# 1. Single quotes
a = 'hello'
print(a)

# 2. Double quotes
b = "hello"
print(b)

# 3. Triple quotes ( Mostly used to write multiline strings )
c = '''hello'''
print(c)

# Slicing a string
"""
Syntax: 
String = "Some String"
Sliced_String = String[start_index:end_index]
Sliced_Character = String[index]

"""

fullName = "John Snoe"
firstName = fullName[0:4] # Slicing from 0 to 4 excluding 4
lastName = fullName[5:9] # Slicing from 5 to 9 excluding 9
character = fullName[0] # Gives the character at index 0
sliced_1 = fullName[:4] # Slicing from 0 to 4 excluding 4, if there is nothing at the start index, python takes the first index
sliced_2 = fullName[5:] # Slicing from 5 to end, if there is nothing at the end index, python takes the last index

print(character)
print("Full Name: ", fullName)
print("Sliced 1: ", sliced_1)
print("First Name: " ,firstName)
print("Sliced 2: ", sliced_2)
print("Last Name: ", lastName)

# Slicing with skip values
"""
Syntax:
String = "Some String"
Sliced_String = String[start_index:end_index:skip_value]

"""

string = "Hello World"
sliced_3 = string[0:11:2] # Skip 2 characters
sliced_4 = string[0:11:3] # Skip 3 characters
sliced_5 = string[0:11:] # Skip 0 characters, if there is nothing at the skip value, python takes it as 0

print(sliced_3)
print(sliced_4)
print(sliced_5)