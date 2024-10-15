# List methods

# Initializing the list
a = [2, 7, 5, 3, 4, 6, 9, 11, 13, 19]
print("Initial list:", a)

# 1. append() - Adds an item to the end of the list
a.append(11)
print("After appending 11:", a)

# 2. extend() - Adds multiple items to the end of the list
a.extend([12, 13, 14])
print("After extending with [12, 13, 14]:", a)

# 3. insert() - Inserts an item at the specified index
a.insert(0, 0)
print("After inserting 0 at index 0:", a)

# 4. remove() - Removes the first item with the specified value
a.remove(0)
print("After removing the first occurrence of 0:", a)

# 5. pop() - Removes the item at the specified index
removed_item = a.pop(0)
print(f"After popping the item at index 0 ({removed_item}):", a)

# 6. sort() - Sorts the list
a.sort()
print("After sorting the list:", a)

# 7. reverse() - Reverses the order of the list
a.reverse()
print("After reversing the list:", a)

# 8. index() - Returns the index of the first item with the specified value
index_of_five = a.index(5)
print("Index of the first occurrence of 5:", index_of_five)

# 9. count() - Returns the number of times the value occurs in the list
count_of_five = a.count(5)
print("Count of occurrences of 5:", count_of_five)

# 10. clear() - Removes all the items from the list
a.clear()
print("After clearing the list:", a)
