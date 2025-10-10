import unittest

from algorithms.queues import (
    ArrayQueue, LinkedListQueue,
    max_sliding_window,
    reconstruct_queue,
    PriorityQueue,
)
from queues.moving_average import MovingAverage


class TestQueue(unittest.TestCase):
    """
        Test suite for the Queue data structures.
    """

    def test_ArrayQueue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())

    def test_arrayqueue_can_grow(self):
        """
        Inserts enough elements for the queue to expand (>10)
        Then extracts them all and ensures they are equal to input values
        """
        q = ArrayQueue()
        for i in range(15):
            q.enqueue(i)

        self.assertSequenceEqual(list(q), range(15))

    def test_arrayqueue_throws_when_empty(self):
        """
        Asserts that an IndexError is thrown when the queue is empty
        Both if it was always empty, as well as if it was dequeued until empty.
        """
        q = ArrayQueue()

        with self.assertRaises(IndexError):
            q.peek()
        with self.assertRaises(IndexError):
            q.dequeue()

        # Assert that it still throws if it once was not empty
        q.enqueue(1)
        q.dequeue()

        with self.assertRaises(IndexError):
            q.peek()
        with self.assertRaises(IndexError):
            q.dequeue()


    def test_LinkedListQueue(self):
        queue = LinkedListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())

    def test_linkedqueue_throws_when_empty(self):
        """
        Asserts that an IndexError is thrown when the queue is empty
        Both if it was always empty, as well as if it was dequeued until empty.
        """
        q = LinkedListQueue()

        with self.assertRaises(IndexError):
            q.peek()
        with self.assertRaises(IndexError):
            q.dequeue()

        # Assert that it still throws if it once was not empty
        q.enqueue(1)
        q.dequeue()

        with self.assertRaises(IndexError):
            q.peek()
        with self.assertRaises(IndexError):
            q.dequeue()


class TestSuite(unittest.TestCase):
    def test_max_sliding_window(self):
        array = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual(max_sliding_window(array, k=5), [5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=7), [6, 7])

        array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
        self.assertEqual(max_sliding_window(array, k=4),
                         [10, 10, 10, 15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=7), [15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=2),
                         [8, 10, 10, 9, 9, 15, 15, 90, 90])

    def test_reconstruct_queue(self):
        self.assertEqual([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
                         reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0],
                                           [6, 1], [5, 2]]))


class TestPriorityQueue(unittest.TestCase):
    """Test suite for the PriorityQueue data structures.
    """

    def test_PriorityQueue(self):
        queue = PriorityQueue([3, 4, 1, 6])
        self.assertEqual(4, queue.size())
        self.assertEqual(1, queue.pop())
        self.assertEqual(3, queue.size())
        queue.push(2)
        self.assertEqual(4, queue.size())
        self.assertEqual(2, queue.pop())

class TestMovingAverage(unittest.TestCase):
    def test_MovingAverage(self):
        m = MovingAverage(3)
        self.assertEqual(m.next(1), 1)
        self.assertEqual(m.next(10), (1 + 10) / 2)
        self.assertEqual(m.next(3), (1 + 10 + 3) / 3)
        self.assertEqual(m.next(5), (10 + 3 + 5) / 3)


if __name__ == "__main__":
    unittest.main()
