# Different dictionary methods

# Creating a dictionary
a = {"name": "John", "age": 36, "country": "Norway"}

# 1. items() - Returns a list containing a tuple for each key value pair
print("Items in the dictionary:", a.items())

# 2. keys() - Returns a list containing the dictionary's keys
print("Keys in the dictionary:", a.keys())

# 3. values() - Returns a list containing the dictionary's values
print("Values in the dictionary:", a.values())

# 4. update() - Updates the dictionary with the specified key-value pairs
a.update({"name": "Jane", "age": 30})
print("Updated dictionary:", a)

# 5. get() - Returns the value of the specified key, if they key does not exists, it will give None
print("Value of key 'name' in the dictionary:", a.get("name"))

# 6. pop() - Removes the element with the specified key
a.pop("age")
print("Updated dictionary:", a)

# 7. clear() - Removes all the elements from the dictionary
a.clear()
print("Updated dictionary:", a)
