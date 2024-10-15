# Random Access Memory (RAM) is volatile and all it contentsare lost once a program terminates, in order to persist the data forever, we user files.

# A file is data stored in a storage device. A python program can talk to the file by reading the contents from it and writing into it.

# Types of files:
# 1. Text files - contains text data (eg. .txt files)
# 2. Binary files - contains binary data (eg. .bin files)

# Opening a file
"""
Syntax: 
open(filename, mode)
"""

""" 
modes: 
r - read mode
w - write mode
a - append mode
r+ - read and write mode
w+ - read and write mode
a+ - append and read mode
b - binary mode
t - text mode
"""

f = open("file.txt", 'r')  # r - read mode
data = f.read()  # read the entire file
print(data)  # print the entire file

f = open("file.txt", 'w')  # w - write mode
f.write("Hello I am writing in the file. ")  # write into the file, it overwrites the previous content, if the file is not present it will create it
f.close()  # close the file

f = open("file.txt", 'a')  # a - append mode
f.write("Hello I am appending the file.")  # append into the file, it appends the previous content, if the file is not present it will create it
f.close()

f = open("file.txt", 'r')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# with statement - automatically closes the file
with open("file.txt", 'r') as f:
    data = f.read()
    print(data)