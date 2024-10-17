# Walrus Operator - The walrus operator is used to assign a value to a variable in one line of code
# It is used in conjunction with the := operator
"""
Syntax:
a = (b := 10) + 5  # a = 15 , b = 10 
"""

if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List length is {n}. It is greater than 3.")