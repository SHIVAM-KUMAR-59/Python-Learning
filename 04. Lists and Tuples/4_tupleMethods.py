# Tuple methods

# Creating a tuple
a = (2, 7, 5, 3, 4, 6, 9, 11, 13, 19)
print("Tuple:", a)

# 1. count() - Returns the number of times a specified value occurs in a tuple
print("Count of 2:", a.count(2))

# 2. index() - Searches the tuple for a specified value and returns the position of where it was found
print("Index of 2:", a.index(2))

# 3. len() - Returns the number of items in the tuple
print("Length of tuple:", len(a))

# 4. max() - Returns the largest item in the tuple
print("Maximum value in tuple:", max(a))

# 5. min() - Returns the smallest item in the tuple
print("Minimum value in tuple:", min(a))

# 6. sum() - Returns the sum of all the items in the tuple
print("Sum of all items in tuple:", sum(a))

# 7. sorted() - Returns a sorted list of the tuple
print("Sorted tuple:", sorted(a))

# 8. Unpacking the tuple
# Unpacking the first two elements into variables and collecting the rest in a list
first, second, *rest = a
print("First element:", first)
print("Second element:", second)
print("Rest of the tuple:", rest)

# 9. tuple() - Converts an iterable into a tuple
list_example = [1, 2, 3, 4, 5]
converted_tuple = tuple(list_example)
print("Converted tuple from list:", converted_tuple)

# 10. reversed() - Returns an iterator that accesses the given tuple in the reverse order
reversed_tuple = tuple(reversed(a))
print("Reversed tuple:", reversed_tuple)
