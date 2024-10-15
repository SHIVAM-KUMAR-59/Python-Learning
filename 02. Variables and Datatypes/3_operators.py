"""
Types of operators:
1. Arithmetic: +, -, *, /, //, **, %
2. Assignment: =, +=, -=, *=, /=, //=, **=, %=
3. Comparison: ==, !=, >, <, >=, <= ( always return boolean value true or false )
4. Logical: and, or, not
5. Bitwise: &, |, ^, ~, <<, >>
"""

a = 10
b = 20
c = a + b # Using arithmetic operator
print(c)

a += 10 # Using assignment operator
print(a)

print(a == b) # Using comparison operator

print(True and False) # Using logical operator

print(True | False) # Using bitwise operator

