# Tuples are immutable data type in Python

b = (1, ) # Tuple with only one element
print(type(b)) # tuple
print(b)

a = (1, "Name", 3.37, False, 5)
print(type(a)) # tuple
print(a)

"""
a[0] = 10 will give error because tuples are immutable and cannot be changed
"""