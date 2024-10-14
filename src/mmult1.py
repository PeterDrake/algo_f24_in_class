def brute_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):  # Row in result
        for j in range(n):  # Column in result
            for k in range(n):  # Element in dot product
                result[i][j] += A[i][k] * B[k][j]
    return result


def mat_add(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):  # Column in result
            result[i][j] = A[i][j] + B[i][j]
    return result


def strassen_mult(A, B):
    if len(A) == 1:
        return brute_mult(A, B)


def get_quadrant(A, vhalf, hhalf):
    """
    :param A: the matrix we're getting a quadrant from
    :param vhalf: vertical half -- 0 for the top half, 1 for the bottom
    :param hhalf: horizontal half -- 0 for left half, 1 for the right
    :return: the indicated submatrix
    """
    mid = len(A)//2
    return [row[mid * hhalf:mid * (hhalf + 1)] for row in A[mid * vhalf:mid * (vhalf + 1)]]


def assemble(upper_left, upper_right, lower_left, lower_right):
    n = len(upper_left)
    result = []
    for i in range(n):
        result += [upper_left[i] + upper_right[i]]

    for i in range(n):
        result +=[lower_left[i] + lower_right[i]]

    return result



    pass
