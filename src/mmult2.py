def brute_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in A]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                result[i][j] += A[i][x] * B[x][j]
    return result


def mat_add(A, B):
    n = len(A)
    result = [[0] * n for _ in A]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    return result


def strassen_mult(a, b):
    if len(a) == 1:
        result = brute_mult(a,b)
    return result


def get_quadrant(a, hhalf, vhalf):
    """
    :param a: the matrix we want a piece of
    :param hhalf: 0 for top, 1 for bottom
    :param vhalf: 0 for left, 1 for right
    :return: that quadrant of the matrix
    """
    n = len(a)
    hstart = hhalf * n//2
    vstart = vhalf * n//2
    return [row[vstart:vstart + n//2] for row in a[hstart:hstart + n//2]]

    # result = [[0] * (n//2) for _ in range(n//2)]
    # for i in range(n//2):
    #     for j in range(n//2):
    #         result[i][j] = a[i + hstart][j + vstart]
    # return result


def assemble(top_left, top_right, bottom_left, bottom_right):
    n = len(top_left)*2
    result = [[]*n]
    for i in range(n):
        if i<len(top_left):
            result[i]=top_left[i] + top_right[i]
        else:
            result[i]=bottom_left[i%len(top_left)] + bottom_right[i%len(top_left)]


