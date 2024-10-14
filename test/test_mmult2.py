from mmult2 import *


def test_brute_mult():
    a = [[2, 3],
         [5, 1]]
    b = [[8, 6],
         [0, 4]]
    assert brute_mult(a, b) == [[16, 24],
                                [40, 34]]


def test_mat_add():
    a = [[2, 3],
         [5, 1]]
    b = [[8, 6],
         [0, 4]]
    assert mat_add(a, b) == [[10, 9],
                             [5, 5]]


def test_1x1():
    a = [[3]]
    b = [[4]]
    assert strassen_mult(a, b) == [[12]]


def test_gets_quadrant():
    a = [[2, 5, 4, 3],
         [6, 9, 0, 2],
         [9, 1, 2, 4],
         [7, 2, 6, 3]]
    assert get_quadrant(a, 0, 1) == [[4, 3],
                                     [0, 2]]

def test_assembles():
    a = [[2, 3],
         [5, 1]]
    b = [[8, 6],
         [0, 4]]
    c = [[2, 3],
         [5, 7]]
    d = [[8, 9],
         [0, 4]]
    assert assemble(a, b, c, d) == [[2, 3, 8, 6],
                                    [5, 1, 0, 4],
                                    [2, 3, 8, 9],
                                    [5, 7, 0, 4]]
