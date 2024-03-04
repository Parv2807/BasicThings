for n in range(0, 5, 1):
    print(end="\n")
    for i in range(0, 5-n, 1):
        print(" ", end=" ")
    for no in range(n+1, 0, -1):
        print(no, end=" ")
    for no2 in range(0, n, 1):
        print(no2+2, end=" ")
