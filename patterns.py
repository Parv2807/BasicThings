#           *
#          ***
#         *****
#          ***
#           *

space = " "
char = "*"


for vi in range(0, 3, 1):
    print(space*(2-vi), char*(2*vi+1))
for vi in range(0, 2, 1):
    print(space*(vi+1), char*(3-2*vi))
"""
for vi in range(0, plus, 1):
    print(space*(minus-vi), char*(2*vi+1))
for vi in range(0, minus, 1):
    print(space*(vi+1), char*(4-(2*vi+1)))
"""