# this program checks weather the string is palindrome or not
a = str(input("enter string"))

check = ""

for i in range(len(a)-1, -1, -1):
    check = check + a[i]

# print(check)

if check == a:
    print("palindrome")