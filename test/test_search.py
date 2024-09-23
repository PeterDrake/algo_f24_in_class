import random
from search import *


def generate(n):
    """
    :return: a list of n random numbers.
    """
    result = [random.random() for _ in range(n)]
    while len(set(result)) < n:
        result = list(set(result))  # Remove duplicates
        result.append(random.random())
    random.shuffle(result)  # Because the conversion to set might have affected the order
    return result


def try_algorithm(f, ls):  # Not a test itself, but called by other tests
    for i, x in enumerate(ls):
        assert f(x, ls) == i
    assert f(-1, ls) == -1
    assert f(1, ls) == -1
    x = random.random()
    while x in ls:
        x = random.random()
    assert f(x, ls) == -1


def test_linear_search_works():
    try_algorithm(linear_search, generate(100))


def test_binary_search_works():
    try_algorithm(binary_search, sorted(generate(100)))


def test_interpolation_search_works():
    try_algorithm(interpolation_search, sorted(generate(100)))
