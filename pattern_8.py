"""
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
"""
rows = 5
num = 1

for i in range(rows):
    for j in range(0,i+1):
        print(num,end=" ")
    num += 2
    print()
