# Walrus Operator - The walrus operator is used to assign a value to a variable in one line of code
# It is used in conjunction with the := operator
"""
Syntax:
a = (b := 10) + 5  # a = 15 , b = 10 
"""

if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List length is {n}. It is greater than 3.")

# Traditional way without walrus operator
numbers = [1, 2, 3, 4, 5]
i = len(numbers)
while i > 0:
    print(f"Remaining count: {i}")
    i -= 1

# Using walrus operator to simplify
numbers = [1, 2, 3, 4, 5]
while (i := len(numbers)) > 0:
    print(f"Remaining count: {i}")
    numbers.pop()  # Remove one item from the list


# Traditional way without walrus operator
data = [5, 10, 15, 20]
results = []
for value in data:
    double = value * 2
    if double > 15:
        results.append(double)

# Using walrus operator inside list comprehension
data = [5, 10, 15, 20]
results = [double for value in data if (double := value * 2) > 15]
print(f"Results using walrus operator: {results}")
