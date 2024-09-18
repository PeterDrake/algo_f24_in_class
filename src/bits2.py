def binary(n):
    value = ''
    while n >= 1:
        value = str(n % 2) + value
        n = n // 2
    return value


class BitVector:

    def __init__(self, bits=0):
        self.bits = bits

    def get(self, i):
        return (self.bits >> i) & 1

    def set(self, i, b):
        self.bits = (self.bits & ~(1 << i)) | (b << i)

    def union(self, other):
        return BitVector(self.bits | other.bits)