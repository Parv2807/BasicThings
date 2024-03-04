n = int(input("entr: "))
a = 1
b = 0
print(b, end=",")
for x in range(0, n, 1):
    a, b = a+b, a
    print(a, end=",")
