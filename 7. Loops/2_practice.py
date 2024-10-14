# 1. WAP to print multiplication table of a number
number = int(input("Enter number: "))

print("Multiplication table of:  ", number)
for i in range(1, 11):
    print(i * number)

# 2. WAP to greet all the person names in a list 'l' which starts with 'S'
l = ["Harry", "Soham", "Sachin", "Manas"]
for i in l:
    if(i.startswith("S")):
        print(f"Hello {i}")

# 3. WAP to check whethe a number is prime or not
number = int(input("Enter a number: "))

# Prime numbers are greater than 1
if number <= 1:
    print("Number is not prime")
else:
    # Loop from 2 to sqrt(number) + 1 to check for divisors
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# 4. WAP to find the factorial of a given number
number = int(input("Enter your number: "))
mul = 1
for i in range(1, number + 1):
    mul *= i

print(mul)

# 5. WAP to print the following pattern:
"""
For n = 3
  *
 ***
*****
"""

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end = " ")
    print("*" * (2*i-1), end = " ")
    print("")

# 6. WAP to print multiplication table of a number in reversed order
number = int(input("Enter number: "))
for i in range(10, 0, -1):
    print(f"{number} X {i} = {number * i}")
