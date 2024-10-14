# Set methods

# 1. add() - Adds an element to the set
a = {1, 2, 3, 4, 5}
a.add(6)
print("Set a after adding 6:", a)

# 2. remove() - Removes an element from the set, raises KeyError if the element is not present
b = {1, 2, 3, 4, 5}
b.remove(3)
print("Set b after removing 3:", b)

# 3. discard() - Removes an element from the set, does nothing if the element is not present
c = {1, 2, 3, 4, 5}
c.discard(3)
print("Set c after discarding 3:", c)

# 4. pop() - Removes and returns an arbitrary(random) element from the set
d = {1, 2, 3, 4, 5}
removed_element = d.pop()
print("Set d after popping an element:", d)
print("Element removed:", removed_element)

# 5. Set membership
e = {1, 2, 3, 4, 5}
print("Is 1 in set e?", 1 in e)
print("Is 6 in set e?", 6 in e)

# 6. Set length
f = {1, 2, 3, 4, 5}
print("Length of set f:", len(f))

# 7. union() - Returns a new set with elements from both sets
g = {1, 2, 3, 4, 5}
h = {6, 7, 8, 9, 10}
i = g.union(h)
print("Set i after union:", i)

# 8. intersection() - Returns a new set with elements common to both sets
j = g.intersection(h)
print("Set j after intersection:", j)

# 9. difference() - Returns a new set with elements in the first set but not in the second set
k = g.difference(h)
print("Set k after difference:", k)

# 10. symmetric_difference() - Returns a new set with elements in either set but not both
l = g.symmetric_difference(h)
print("Set l after symmetric difference:", l)
