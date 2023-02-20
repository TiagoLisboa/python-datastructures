import unittest
import random
from bubblesort.main import bubblesort

class BubbleSortTestCase(unittest.TestCase):

    def test_sort_1(self):
        array = [2, 4, 3, 5, 1, 9]

        sorted_array = bubblesort(array)


        self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 9])

    def test_sort_2(self):
        array = [random.choice(range(100)) for _ in range(100)]

        sorted_array = bubblesort(array)


        self.assertEqual(sorted_array, sorted(array))
