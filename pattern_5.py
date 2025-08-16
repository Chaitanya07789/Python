"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""
rows = 5
num = 0
for i in range(rows ,0 ,-1):
    num += 1
    for j in range(1 ,i+1):
        print(num ,end=" ")
    print()
