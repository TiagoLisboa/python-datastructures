import unittest
from binarysearchtree.main import BinarySearchTree

class SearchTreeTestCase(unittest.TestCase):

    def test_insert(self):
        tree = BinarySearchTree()

        tree.insert(3)
        tree.insert(2)
        tree.insert(1)
        tree.insert(9)
        tree.insert(4)
        tree.insert(5)


        self.assertEqual(tree.len(), 6)
        self.assertEqual(tree.inorder(), [1, 2, 3, 4, 5, 9])
