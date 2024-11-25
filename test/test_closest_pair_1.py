from closest_pair_1 import *
import math
import random


def test_finds_right_distance():
    assert distance(1, 1, 2, 2) == math.sqrt(2)


def test_finds_right_pair():
    points = [(1, 1), (1, 2), (1, 4), (3, 3), (4, 1)]
    assert closest_pair(points) == [(1, 1), (1, 2)]


def test_works_on_larger_set():
    random.seed(0)
    points = [(random.random(), random.random()) for _ in range(10000)]
    print(closest_pair(points))
