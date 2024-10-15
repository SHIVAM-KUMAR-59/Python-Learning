
# Generate tables from 1 to 20 and write them in a file

def generate_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    with open (f"Table/table_of_{n}.txt", "w") as f:
        f.write(f"Table of {n}:\n")
        f.write(table)

for i in range(1, 21):
    generate_table(i)