import matplotlib.pyplot as plt
from math import log


plt.plot([log(n) for n in range(1, 101)])
plt.plot([n for n in range(1, 101)])
plt.show()
