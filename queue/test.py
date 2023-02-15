import unittest

from queue.main import Queue


class QueueTestCase(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()

        self.assertEqual(queue.len(), 0)
        queue.enqueue(1)
        self.assertEqual(queue.len(), 1)

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue(1)
        self.assertEqual(queue.len(), 1)
        queue.dequeue()
        self.assertEqual(queue.len(), 0)

    def test_front(self):
        queue = Queue()

        queue.enqueue(1)
        self.assertEqual(queue.front(), 1)

        queue.enqueue('test')
        self.assertEqual(queue.front(), 'test')

        queue.dequeue()
        self.assertEqual(queue.front(), 'test')
