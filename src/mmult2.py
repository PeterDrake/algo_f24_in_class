import numpy as np


def multiplication(A, B):
    n = len(A)
    result = [[0] * n for _ in A]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                result[i][j] += A[i][x] * B[x][j]
    return result



a = [[2, 3],
     [5, 1]]

b = [[8, 6],
     [0, 4]]

# a = np.array(a)
# b = np.array(b)

print(multiplication(a, b))
