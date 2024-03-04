# this programs removes all occurrences of a char in a string
a = str(input("Enter required string: "))
char = input("enter character to be deleted: ")
output = ""

for i in a:
    if i != char:
        output = output + i

print(output)
