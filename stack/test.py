import unittest

from stack.main import Stack


class StackTestCase(unittest.TestCase):
    def test_push(self):
        stack = Stack()

        self.assertEqual(stack.len(), 0)
        stack.push(1)
        self.assertEqual(stack.len(), 1)

    def test_pop(self):
        stack = Stack()

        stack.push(1)
        self.assertEqual(stack.len(), 1)
        stack.pop()
        self.assertEqual(stack.len(), 0)
