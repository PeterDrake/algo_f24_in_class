import matplotlib.pyplot as plt
from math import log

plt.plot([log(n) for n in range(1, 101)], label='$log(n)$')
plt.plot([n for n in range(1, 101)], label='$n$')
plt.plot([n ** 2 for n in range(1, 101)], label='$n^2$')
plt.legend()
plt.show()
