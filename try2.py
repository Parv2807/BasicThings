# wap a program to find lcm and hcf of two numbers

m = int(input("enter number:"))
n = int(input("enter number:"))


def lcm_of_nos(x, y):
    small = min(x, y)
    i = small
    while True:
        if i % y == 0:
            if i % x == 0:
                lcm = i
                break
            else:
                i += 1
        else:
            i += 1
    return lcm


def hcf_of_nos(x, y):
    small = min(x, y)
    hcf = None
    for j in range(1, small+1, 1):
        if x % j == 0:
            if y % j == 0:
                hcf = j
    return hcf


print("lcm is", lcm_of_nos(m, n))
print("hcf is", hcf_of_nos(m, n))
