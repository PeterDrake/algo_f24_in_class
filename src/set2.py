class Set:
    def __init__(self):
        self.set = []

    def add(self, other):
        if other not in self.set:
            self.set.append(other)

    def remove(self, other):
        return self.set.remove(other)

    def contains(self, value):
        return value in self.set
