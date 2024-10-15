# type() function is used to identify the datatype of a variable

a = 10
b = 10.5
c = "10"
d = True
e = False
f = None

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'bool'>
print(type(e)) # <class 'bool'>
print(type(f)) # <class 'NoneType'>

# Typecasting - Converting one data type to another
a = 10
b = 10.5
c = "10"
d = True
e = False
f = None

print(type(int(a))) # <class 'int'>
print(type(float(b))) # <class 'float'>
print(type(str(a))) # <class 'str'>
print(type(bool(d))) # <class 'bool'>
