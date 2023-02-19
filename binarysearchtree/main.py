from __future__ import annotations


class Node():
    value: int
    left: Node | None
    right: Node | None
    parent: Node | None

    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent


class BinarySearchTree():
    root: Node | None
    size: int = 0

    def __init__(self):
        self.root = None
        self.size = 0

    def len(self):
        return self.size

    def search(self, value, node):
        if node.value is None or node.value == value:
            return node

        if value < node.value:
            return self.search(value, node.left)

        return self.search(value, node.right)


    def insert(self, value):
        node = Node(value)
        node.left = Node(None, node)
        node.right = Node(None, node)
        if not self.root:
            self.root = node
            self.size += 1
            return

        foundNode = self.search(value, self.root)

        if foundNode.value is None:
            foundNode.value = value
            foundNode.left = Node(None, foundNode)
            foundNode.right = Node(None, foundNode)
            self.size += 1

    def inorder(self, node: Node | None = None):
        if node == None:
            node = self.root

        if node.value:
            left = self.inorder(node.left)
            right = self.inorder(node.right)
            return left + [node.value] + right

        return []








