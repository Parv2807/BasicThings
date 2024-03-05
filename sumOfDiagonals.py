# wap to input a matrix from the user and print its sum

n = int(input("enter number of rows and columns: "))
data = []
for x in range(0, n, 1):
    d1 = []
    for y in range(0, n, 1):
        print(x, ",", y, end=" -- ")
        d = int(input("enter number: "))
        d1.append(d)
    data.append(d1)

# printing the matrix
for x in range(0, n, 1):
    print(end="\n")
    for y in range(0, n, 1):
        print(data[x][y], end="\t\t\t")

# summing the diagonals
s = 0

# top-right to bottom-left
for x in range(0, n, 1):
    s += data[x][x]

# top-left to bottom-right
for x in range(0, n, 1):
    s += data[x][n-x-1]

# subtracting the middle the element as it adds twice
# the repetition only occurs if it is a odd x odd type matrix

s1 = int((n-1)/2)

if n % 2 == 1:
    s = s-data[s1][s1]

print("\n")
print(s)
