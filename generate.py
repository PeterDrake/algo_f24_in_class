import random
import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, 'w') as f:
    for i in range(n):
        print(random.randint(0, 999999), file=f)
