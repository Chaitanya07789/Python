matrix1 = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]
matrix2 = [
    [2,2,2],
    [1,1,1],
    [3,3,3]
]
matrix3 = matrix1 + matrix2 # combines 2 matrix [[1, 1, 1], [2, 2, 2], [3, 3, 3], [2, 2, 2], [1, 1, 1], [3, 3, 3]]
print(matrix3)

#  used for creating matrix of same size 
result = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2))]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(result)
