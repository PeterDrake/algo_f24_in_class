import math


def closest_pair(array):
    least = float("inf")
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            d = distance(*array[i], *array[j])
            if d < least:
                least = d
                least_pair = [array[i], array[j]]
    return least_pair


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

