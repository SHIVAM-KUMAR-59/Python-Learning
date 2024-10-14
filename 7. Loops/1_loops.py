# Loops -  loops are used to repeat a block of code multiple times. 

# 1. For loop
"""
Syntax:
for i in range(start, stop, step):
    Write your commands
"""

for i in range(1, 6): # Prints number from 1 to 5, 6 is not included
    print(i)

# 2. While loop
"""
Syntax:
while condition:
    Write your commands
"""

i = 0
while i < 6: # Prints number from 1 to 5, 6 is not included
    print(i)
    i += 1 # It is important to update the value of i after each iteration, because if we don't do it, the loop will run forever

# Print the contents of a list
list = [1, 2, 3, 4, 5, 6]
print("Using for loop")
for i in list:
    print(i)

print("Using while loop")
i = 0
while (i < len(list)):
    print(list[i])
    i += 1

# 3. Break and continue

# Break - Breaks out of the loop
for i in range(10):
    if(i == 5):
        break # It breaks out of the loop
    print(i)

# Continue - Continues with the next iteration
for i in range(10):
    if(i == 5):
        continue # It continues with the next iteration
    print(i)