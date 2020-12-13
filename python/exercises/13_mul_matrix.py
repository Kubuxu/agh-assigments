import random

def randMatrix(size):
    return [[random.randrange(20) for _ in range(size)] for _ in range(size)]

size = 8
matrix1 = randMatrix(size)
matrix2 = randMatrix(size)

# identity matrix
#matrix2 = [[1 if x == y else 0 for x in range(size)] for y in range(size)]

print("Matrix1")
print(*matrix1, sep='\n')
print("Matrix2")
print(*matrix2, sep='\n')

res = [[0 for _ in range(size)] for _ in range(size)]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]


print("Matrix1*Matrix2")
print(*res, sep='\n')
