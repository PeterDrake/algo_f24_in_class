# Adapted from Sedgewick & Wayne, Algorithms
import random


def selection_sort(a, key=lambda x: x):
    n = len(a)
    for i in range(n):
        min_ = i
        for j in range(i + 1, n):
            if key(a[j]) < key(a[min_]):
                min_ = j
        a[i], a[min_] = a[min_], a[i]


def insertion_sort(a, key=lambda x: x):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if key(a[j - 1]) <= key(a[j]):
                break
            a[j], a[j - 1] = a[j - 1], a[j]


def merge(a, aux, lo, mid, hi, key):
    aux[lo:hi + 1] = a[lo:hi + 1]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif key(aux[j]) < key(aux[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


def mergesort(a, key=lambda x: x):
    def f(lo, hi):
        if hi <= lo:
            return
        mid = (lo + hi) // 2
        f(lo, mid)
        f(mid + 1, hi)
        merge(a, aux, lo, mid, hi, key)
    aux = a[:]
    f(0, len(a) - 1)


def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randint(i, n - 1)
        a[i], a[r] = a[r], a[i]


def quicksort(a, key=lambda x: x):
    def f(a):
        if len(a) <= 1:
            return a
        pivot = a[0]
        # There are ways to do this faster and in place, but they don't change the order
        left = [x for x in a if key(x) < key(pivot)]
        same = [x for x in a if key(x) == key(pivot)]
        right = [x for x in a if key(x) > key(pivot)]
        return f(left) + same + f(right)
    shuffle(a)
    return f(a)
