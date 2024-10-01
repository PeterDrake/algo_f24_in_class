from sort import *
from time import time
import matplotlib.pyplot as plt


def time_function(f, ns):
    result = []
    for n in ns:
        a = [random.random() for _ in range(n)]
        before = time()
        f(a)
        result.append(time() - before)
    return result


ns = range(100, 2001, 100)

for f in [selection_sort, insertion_sort, mergesort, quicksort]:
    plt.plot(ns, time_function(f, ns), label=str(f))

plt.legend()
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.show()
