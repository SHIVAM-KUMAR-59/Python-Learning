# List - Lists are containers to store a collection of items in a particular order 

# 1. Creating a list
a = [1, "Name", 3.37, False, 5]
print(a)

a[0] = 10 # Lists unlike strings, are mutable
print(a)

# 2. List slicing ( same as strings )
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b[0:5]) # Prints from index 0 to 4
print(b[5:]) # Prints from index 5 to end