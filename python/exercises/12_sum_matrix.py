import random

def randMatrix(size):
    return [[random.random() for _ in range(size)] for _ in range(size)]

matrix1 = randMatrix(5)
matrix2 = randMatrix(5)
print("Matrix1")
print(*matrix1, sep='\n')
print("Matrix2")
print(*matrix2, sep='\n')

# trivial with numpy but let's play
sumMatrix = [ [v1+v2 for v1, v2 in zip(*row)] for row in zip(matrix1, matrix2) ]
print("Matrix1+Matrix2")
print(*sumMatrix, sep='\n')
