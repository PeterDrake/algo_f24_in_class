class mySet:

    def __init__(self, data=[]):
        self.data = [False] * 100
        for item in data:
            self.data[item] = True

    def add(self, item):
        self.data[item] = True

    def remove(self, item):
        self.data[item] = False

    def contains(self, item):
        return self.data[item]
