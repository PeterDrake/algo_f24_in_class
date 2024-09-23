class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

    # def item(self, item):
    #     self.item = item
    # def next(self, next):
    #     self.next = next


class LinkedSet:

    def __init__(self):
        self._top = None

    def contains(self, item):
        currentNode = self._top
        while currentNode:
            if (currentNode.item == item):
                return True
            currentNode = currentNode.next
        return False

    def add(self, item):
        self.currentNode = self._top
        while (1):
            if (self.currentNode == None):
                self.newNode = Node(item, self._top)
                self._top = self.newNode
                break
            if(self.currentNode.item == item):
                break
            self.currentNode = self.currentNode.next


    def remove(self, item):
        self.currentNode = self._top
        if(self.currentNode.item == item):
            self._top = self.currentNode.next
        else:
            while (1):
                if (self.currentNode.next == None):
                    break
                if (self.currentNode.next.item == item):
                    self.currentNode.next = self.currentNode.next.next
                    break
                self.currentNode = self.currentNode.next