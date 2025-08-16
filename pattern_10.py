"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
rows = 5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

# or 
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()