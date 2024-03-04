# wap to enter elements from the user and print the maximum and minimum element
l = []

while True:
    n = int(input("enter number:"))
    if n == 0:
        break
    else:
        l.append(n)
print(l)
# bubble sorting

for i in range(0, len(l), 1):
    for j in range(i, len(l), 1):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print("largest number is:", l[len(l)-1])
print("smallest number is: ", l[0])
