class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Set():
    def __init__(self):
        self.top = None

    def add(self, value):
        if not self.contains(value):
            self.top = Node(value, self.top)

    def remove(self, value):
        if self.contains(value):
            node = self.top
            while node:
                if node.item == value:
                    previous.next = node.next
                    return
                previous = node
                node = node.next

    def contains(self, value):
        node = self.top
        while node:
            if node.item == value:
                return True
            node = node.next
        return False

    def __str__(self):
        string = "{"
        node = self.top
        while node:
            string += str(node.item)
            if node.next:
                string += ", "
            node = node.next
        string += "}"
        return string


x = Set()
x.add(5)
x.add(6)
x.add(7)
x.add(6)
print(str(x))
x.remove(6)
print(str(x))
