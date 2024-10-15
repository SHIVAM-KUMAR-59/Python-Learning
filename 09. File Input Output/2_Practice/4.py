# A file contains the word 'Donkey' multiple times, you have to replace this word with '#######'

word = 'donkey'

with open ("file.txt", 'r') as f:
    content = f.read()
    newContent = content.replace(word, "#######")

with open ("file.txt", 'w') as f:
    f.write(newContent)