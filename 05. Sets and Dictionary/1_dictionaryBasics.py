# Dictionary are a collection of key-value pairs
"""
Syntax:
Dictionary = {key1: value1, key2: value2, key3: value3}
"""

"""
Properties:
1. Keys are unique
2. Keys can be of any data type
3. Cannot contain duplicate keys
3. It is unordered
4. It is mutable
5. It is indexed
"""

# Creating a dictionary
a = {"name": "John", "age": 36, "country": "Norway"}

# Checking the type of the variable
print("Type of variable 'a':", type(a))

# Printing the entire dictionary
print("Dictionary:", a)

# Accessing and printing values using keys
print("Name:", a["name"])
print("Age:", a["age"])
print("Country:", a["country"])

# Changing the value of a key and printing the updated value
a["age"] = 37
print("Updated Age:", a["age"])
