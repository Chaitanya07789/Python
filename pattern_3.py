"""
1 2 3
4 5 6
7 8 9
10 11 12
"""
rows = 4
num = 1
for i in range(rows):
    for j in range(rows-1):
        print(num, end=" ")
        num +=1
    print()


