import matplotlib.pyplot as plt
from math import log


# plt.plot([1, 3, 2])
plt.plot(range(2, 1001), [log(x) for x in range(2, 1001)])
plt.plot(range(2, 1001), [log(log(x)) for x in range(2, 1001)])
plt.show()

