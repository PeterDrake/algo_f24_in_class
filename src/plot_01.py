import matplotlib.pyplot as plt
from math import log

# plt.plot([log(n) for n in range(1, 101)], label='$log(n)$')
# plt.plot([n for n in range(1, 101)], label='$n$')
# plt.plot([n ** 2 for n in range(1, 101)], label='$n^2$')
# plt.legend()
# plt.show()

from time import time
from fibo import *


def time_function(f, n):
    start = time()
    f(n)
    return time() - start


for f in [fibo_rec, fibo_iter, fibo_small, fibo_formula]:
    plt.plot(range(1, 21), [time_function(f, n) for n in range(1, 21)], label=str(f))
plt.legend()
plt.show()
