
# 1. WAP to find the greatest of 4 numbers entered by the user

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a > b and a > c and a > d):
    print("a is greatest and it's value is: ", a)
elif(b > a and b > c and b > d):
    print("b is greatest and it's value is: ", b)
elif(c > a and c > b and c > d):
    print("c is greatest and it's value is: ", c) 
else:
    print("d is greatest and it's value is: ", d)

# 2. WAP to find out whether a student has passed or failed if it requires an average of 40% and at least 33% in each subject.Assume 3 subjects and take marks as input from the user

a = int(input("Enter marks in subject 1: "))
b = int(input("Enter marks in subject 2: "))
c = (int(input("Enter marks in subject 3: ")))

total_marks = a + b + c

if(a < 33 or b < 33 or c < 33):
    print("Student has failed")
elif(total_marks / 3 < 40):
    print("Student has failed")
else:
    print("Student has passed")

# 3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "Buy Now", "Subscribe this", "Click this". WAP to detect these spams

comment = input("Enter your comment: ")

if("Make a lot of money" in comment):
    spam = True
elif("Buy Now" in comment):
    spam = True
elif("Subscribe this" in comment):
    spam = True
elif("Click this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# 4 WAP to find whether a username contains less than 10 characters

username = input("Enter your username")

if(len(username) < 10):
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")

# 5. WAP to find whether a fruit is present in the list or not

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
name = input("Enter fruit name")
if(name in list):
    print("Fruit is present in the list")
else:
    print("Fruit is not present in the list")

# 6. WAP to calculate the grade of a student based on marks from the following scheme:
"""
90-100: Grade E
80-90: Grade A
70-80: Grade B
60-70: Grade C
50-60: Grade D
<50: Grade F
"""

marks = int(input("Enter marks obtained: "))
if(marks > 100 or marks < 0):
    print("Invalid marks")
elif(marks >= 90):
    print("Grade E")
elif(marks >= 80 and marks < 90):
    print("Grade A")
elif(marks >= 70 and marks < 80):
    print("Grade B")
elif(marks >= 60 and marks < 70):
    print("Grade C")
elif(marks >= 50 and marks < 60):
    print("Grade D")
else:
    print("Grade F")