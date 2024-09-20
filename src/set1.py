class Set():
    def __init__(self):
        self.ls = []

    def add(self, item):
        for x in self.ls:
            if item == x:
                return
        self.ls.append(item)

    def remove(self, item):
        for x in self.ls:
            if item == x:
                self.ls.remove(x)

    def contains(self, item):
        for x in self.ls:
            if item == x:
                return True
        return False
