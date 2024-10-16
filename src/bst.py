# Based on Sedgewick & Wayne's BST.java

class BST:

    class _Node:
        def __init__(self, key, left=None, right=None):
            self.left = left
            self.key = key
            self.right = right

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
            return node
        self.root = f(self.root)

    def _remove_min(self, node):
        """
        :return: A version of node and its descendants, but with the smallest key remove.
        """
        if node.left is None:
            return node.right
        node.left = self._remove_min(node.left)
        return node

    def _min_node(self, node):
        """
        :return: The _Node containing the smallest key in the subtree rooted at node.
        """
        if node.left is None:
            return node
        return self._min_node(node.left)

    def remove(self, key):
        def f(node):
            if node is None:
                return node
            if key < node.key:
                node.left = f(node.left)
            elif key == node.key:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = node
                node = self._min_node(temp.right)
                node.right = self._remove_min(temp.right)
                node.left = temp.left
            else:
                node.right = f(node.right)
            return node
        self.root = f(self.root)
