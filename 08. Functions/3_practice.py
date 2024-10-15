# 1. WAP to find greatest of 3 numbers

def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > c):
        return b
    else: return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(greatest(a, b, c))

# 2. WAP to convert celsius to farenhein
def celisun_to_farenheit_converter(a):
    return (a * 9/5) + 32

a = int(input("Enter temperature in celsius: "))
print(f"{a} celsius in farenheit is: {celisun_to_farenheit_converter(a)}")

# 3. WAP to comvert inches to cms
def inches_to_cms(a):
    return a * 2.54

a = int(input("Enter inches: "))
print(f"{a} inches in cms is: {inches_to_cms(a)}")

# 4. WAP to remove a given word from the list and strip it at the same time
def remove_and_strip(l, word):
    n = []
    for item in l:
        if item in l:
            if(item != word):
                n.append(item.strip(word))
    return l

l = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
word = input("Enter word to remove and strip: ")
print(remove_and_strip(l, word))

# 5. WAP to print multiplication table of a given number
def multiplication(a):
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")

a = int(input("Enter number: "))
multiplication(a)