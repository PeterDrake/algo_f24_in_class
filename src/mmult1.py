def mat_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):  # Row in result
        for j in range(n):  # Column in result
            for k in range(n):  # Element in dot product
                result[i][j] += A[i][k] * B[k][j]
    return result


if __name__ == "__main__":
    # A = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    #
    # B = [
    #     [9, 8, 7],
    #     [6, 5, 4],
    #     [3, 2, 1]
    # ]

    A = [[1, 2],
         [5, 3]]

    B = [[4, 2],
         [1, 6]]

    result = mat_mult(A, B)

    print("Result of matrix multiplication:")
    for row in result:
        print(row)



