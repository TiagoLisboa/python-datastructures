from heap.main import Heap

import unittest

class HeapTestCase(unittest.TestCase):
    def test_insert(self):
        heap = Heap()

        self.assertEqual(heap.len(), 0)
        heap.insert(2)
        self.assertEqual(heap.len(), 1)
        self.assertEqual(heap.list[0], 2)
        heap.insert(1)
        self.assertEqual(heap.len(), 2)
        self.assertEqual(heap.list[0], 2)
        heap.insert(3)
        self.assertEqual(heap.len(), 3)
        self.assertEqual(heap.list[0], 3)

    def test_extract_max(self):
        heap = Heap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(15)
        heap.insert(13)
        heap.insert(3)
        heap.insert(99)
        heap.insert(4)

        max = heap.extract_max()
        self.assertEqual(max, 99)
        self.assertEqual(heap.len(), 6)
        self.assertEqual(heap.list[0], 15)
