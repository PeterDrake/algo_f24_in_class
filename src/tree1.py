class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.left} {self.key} {self.right}]'

    def __repr__(self):
        return str(self)


t = Node('A',
         Node('B', Node('D', right=Node('G'))),
         Node('C', Node('E', Node('H'), Node('I')),
              Node('F', Node('J'))))

print(t)

from collections import deque

def level_order(t):
    result = []
    if t:
        d = deque()
        d.append(t)
        while len(d):
            n = d.popleft()
            result.append(n.key)
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)
    return result

def preorder(t):
    def f(n):
        if n is None:
            return
        result.append(n.key)
        f(n.left)
        f(n.right)
    result = []
    f(t)
    return result

def inorder(t):
    def f(n):
        if n is None:
            return
        f(n.left)
        result.append(n.key)
        f(n.right)
    result = []
    f(t)
    return result

def postorder(t):
    def f(n):
        if n is None:
            return
        f(n.left)
        f(n.right)
        result.append(n.key)
    result = []
    f(t)
    return result