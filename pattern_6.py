"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
rows = 5
num = rows

# for i in range(rows):
#     for j in range(rows):
#         print(num,end=" ")
#     rows-=1
#     print()

for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=" ")
    print()


