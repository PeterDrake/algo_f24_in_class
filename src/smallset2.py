class SmallSet:
    def __init__(self):
        self.data = [False] * 100

    def add(self, item):
        self.data[item] = True

    def remove(self, item):
        self.data[item] = False

    def contains(self, item):
        return self.data[item]

    # def __str__(self):
    #     s = ''
    #     for x in self.data:
    #         s += self.data[x]