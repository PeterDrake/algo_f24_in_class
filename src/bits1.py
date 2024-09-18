def binary(n):
    if n >= 1:
        return binary(n // 2) + str(n % 2)
    return ''

class BitVector:

    def __init__(self, bits=0):
        self.bits = bits

    def get(self, i):
        return (self.bits >> i) & 1

    def set(self, i, b):
        self.bits = (self.bits & ~(1 << i)) | (b << i)

    def union(self, other):
        return BitVector(self.bits | other.bits)
