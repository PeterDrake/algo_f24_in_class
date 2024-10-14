from mmult1 import *


def test_brute_mult():
    A = [[1, 2],
         [5, 3]]
    B = [[4, 2],
         [1, 6]]
    assert brute_mult(A, B) == [[6, 14], [23, 28]]


def test_mat_add():
    A = [[1, 2],
         [5, 3]]
    B = [[4, 2],
         [1, 6]]
    assert mat_add(A, B) == [[5, 4], [6, 9]]


def test_mult_1x1():
    A = [[2]]
    B = [[3]]
    assert strassen_mult(A, B) == [[6]]


def test_gets_quadrant():
    A = [[1, 2, 3, 4],
         [5, 3, 0, 8],
         [6, 2, 4, 1],
         [7, 8, 1, 3]]
    assert get_quadrant(A, 0, 1) == [[3, 4], [0, 8]]


def test_gets_lower_right_quadrant():
    A = [[1, 2, 3, 4],
         [5, 3, 0, 8],
         [6, 2, 4, 1],
         [7, 8, 1, 3]]
    assert get_quadrant(A, 1, 1) == [[4, 1], [1, 3]]


def test_assembles_matrix():
    A = [[1, 2],
         [5, 3]]
    B = [[1, 0],
         [4, 3]]
    C = [[1, 7],
         [5, 8]]
    D = [[6, 9],
         [5, 3]]
    assert assemble(A, B, C, D) == [[1, 2, 1, 0],
                                    [5, 3, 4, 3],
                                    [1, 7, 6, 9],
                                    [5, 8, 5, 3]]
