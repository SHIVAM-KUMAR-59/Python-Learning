# Sets are a collection of non-repetitive elements

"""
Syntax:
Set = {element1, element2, element3}
"""

"""
Properties:
1. Elements are unique
2. Elements can be of any data type
3. It is unordered
4. There is no way to change items in sets
5. It is un-indexed - Cannot access elements by index
"""

# Empty set
# a = {} This will be considered as a dictionary
a = set()  # Correct way to create an empty set

# 1. Creating a set
a = {1, "Name", 3.37, False, 5}
print("Type: ", type(a))
print("Set a:", a)

# 2. Set slicing (Note: Sets are unordered, so slicing doesn't work with sets)
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Slicing cannot be performed on sets because they are unordered collections.
# Removing set slicing examples since it's not applicable for sets.

# 3. Set operations
c = {1, 2, 3, 4, 5}
d = {2, 4, 6, 8, 10}
print("Set c:", c)
print("Set d:", d)
print("Union of c and d (c | d):", c | d)  # Union
print("Intersection of c and d (c & d):", c & d)  # Intersection
print("Difference of c and d (c - d):", c - d)  # Difference
print("Symmetric difference of c and d (c ^ d):", c ^ d)  # Symmetric difference
