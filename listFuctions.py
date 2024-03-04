# this program replaces all the even elements with sum of digits and odd elements with product of digits
a = [100, 43, 20, 56, 32, 91, 80, 40, 45, 21]
b = []
for i in a:
    if i % 2 == 0:
        s = 0
        while i > 0:
            s = s + i % 10
            i = i // 10
        b.append(s)
    else:
        p = 1
        while i > 0:
            p = p * (i % 10)
            i = i // 10
        b.append(p)

print(b)
