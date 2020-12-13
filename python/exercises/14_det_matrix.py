import random
import copy
import numpy as np

def randMatrix(size):
    return [[random.randrange(20) for _ in range(size)] for _ in range(size)]

size = 5
matrix = randMatrix(size)

# identity matrix
#matrix2 = [[1 if x == y else 0 for x in range(size)] for y in range(size)]

print("Matrix")
print(*matrix, sep='\n')

def det(A):
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    D = 0
    for i in range(len(A)):
        Dtmp = copy.deepcopy(A)

        del Dtmp[0] # remove first row
        for row in Dtmp: del row[i] # remove i-th column

        o = A[0][i]
        o *= (-1)**i
        o *= det(Dtmp)

        D += o

    return D



print("|Matrix|")
print(det(matrix))
print("|Matrix| from np")
print(np.linalg.det(np.array(matrix)))
