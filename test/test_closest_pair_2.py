from closest_pair_2 import clos_pair_bruteforce
import random


def test_finds_closest_pair_in_small_set():
    points = [(0, 0), (1, 5), (3, 2), (4, 3), (3, 5)]
    clos_points, distance = clos_pair_bruteforce(points)
    assert clos_points == ((3, 2), (4, 3))


def test_finds_closest_pair_in_large_set():
    random.seed(0)
    points = [(random.random(), random.random()) for _ in range(100)]
    clos_points, distance = clos_pair_bruteforce(points)
    correct = ((0.7197046864039541, 0.39882354222426875), (0.7156193503014563, 0.38801723531250565))
    assert set(clos_points) == set(correct)
