# WAP to read the text from a file named 'poem.txt' and check whethe the word 'twinkle' is present or not.

f = open("poem.txt", 'r')
data = f.read()
f.close()

if('twinkle' in data):
    print("Yes, 'twinkle' is present in the poem")
else:
    print("No, 'twinkle' is not present in the poem")