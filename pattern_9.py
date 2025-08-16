"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
rows = 5
for i in range(rows+1):
    num = i
    for j in range(1,i+1):
        print(num,end=" ")
        num -= 1
    print()

# or

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")

