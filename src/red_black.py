class RedBlackBST:

    class _Node:
        RED = True
        BLACK = False
        def __init__(self, key, left=None, right=None, color=RED):
            self.left = left
            self.key = key
            self.right = right
            self.color = color

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def contains(self, key):
        def f(node):
            if node is None:
                return False
            if key < node.key:
                return f(node.left)
            elif key == node.key:
                return True
            else:
                return f(node.right)
        return f(self.root)

    def _is_red(self, node):
        return (node is not None) and node.color

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self._Node.RED
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self._Node.RED
        return x

    def _flip_colors(self, node):
        node.color = self._Node.RED
        node.left.color = self._Node.BLACK
        node.right.color = self._Node.BLACK

    def add(self, key):
        def f(node):
            if node is None:
                return self._Node(key)
            if key < node.key:
                node.left = f(node.left)
            elif key == node.key:
                pass
            else:
                node.right = f(node.right)
            if self._is_red(node.right) and not self._is_red(node.left):
                node = self._rotate_left(node)
            if self._is_red(node.left) and self._is_red(node.left.left):
                node = self._rotate_right(node)
            if self._is_red(node.left) and self._is_red(node.right):
                self._flip_colors(node)
            return node
        self.root = f(self.root)
        self.root.color = self._Node.BLACK
