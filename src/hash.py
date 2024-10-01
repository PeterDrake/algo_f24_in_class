class ChainedHashSet:
    def __init__(self, table_size):
        self.table = [[] for _ in range(table_size)]

    def contains(self, key):
        i = abs(hash(key)) % len(self.table)
        return key in self.table[i]

    def add(self, key):
        i = abs(hash(key)) % len(self.table)
        if key not in self.table[i]:
            self.table[i].append(key)

    def remove(self, key):
        i = abs(hash(key)) % len(self.table)
        if key in self.table[i]:
            self.table[i].remove(key)
