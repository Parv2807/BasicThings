# Write a python program to create a dictionary STUDENT containing StudentNames as keys and
# corresponding Marks as values. The program should create a list , of those StudentNames for
# which Marks is less than 33.
rec = {}
fails = []
n = int(input("enter no. of students: "))

for x in range(0, n, 1):
    name = str(input("enter name "))
    marks = float(input("enter marks: "))
    rec[name] = marks

for i in rec.keys():
    if rec[i] < 33:
        name = i
        marks = rec[i]
        ele = [name, marks]
        fails.append(ele)


for i in fails:
    print(i[0], "\t", i[1])
