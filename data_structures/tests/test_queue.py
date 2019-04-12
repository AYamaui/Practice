import unittest
import sys
sys.path.append('../')
import my_queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = my_queue.Queue()
        self.queue.enqueue(2)
        self.queue.enqueue(11)
        self.queue.enqueue(33)
        self.queue.enqueue(16)
        self.queue.enqueue(89)
        self.queue.enqueue(23)

    def test_enqueue_empty_queue(self):
        _queue = my_queue.Queue()
        previous_size = _queue.size
        _queue.enqueue(18)
        self.assertEqual(_queue.tail.value, 18)
        self.assertTrue(_queue.size == (previous_size + 1))

    def test_enqueue(self):
        previous_size = self.queue.size
        self.queue.enqueue(18)
        self.assertEqual(self.queue.tail.value, 18)
        self.assertTrue(self.queue.size == (previous_size + 1))

    def test_deque_empty_queue(self):
        _queue = my_queue.Queue()

        with self.assertRaises(Exception) as context:
            _queue.deque()

        self.assertEqual('Empty queue', str(context.exception))

    def test_deque(self):
        previous_size = self.queue.size
        element = self.queue.deque()
        self.assertEqual(element, 2)
        self.assertEqual(self.queue.head.value, 11)
        self.assertTrue(self.queue.size == (previous_size - 1))

    def test_is_empty_empty_queue(self):
        _queue = my_queue.Queue()
        self.assertTrue(_queue.is_empty())

    def is_empty(self):
        self.assertFalse(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
