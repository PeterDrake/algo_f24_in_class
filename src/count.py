def count():
    count.n += 1
    return count.n

count.n = 0

class Tricky:
    def __init__(self):
        self.x = 3

    def __eq__(self, other):
        return self.x == other.x
