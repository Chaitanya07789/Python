"""
1
3 2
6 5 4
10 9 8 7
"""
rows = 4
count = 1

for i in range(1,rows+1):
    start = count + i -1
    for j in range(start,count-1,-1):
        print(j,end=" ")
    print()
    count = start + 1