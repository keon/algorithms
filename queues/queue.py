"""
Queue Abstract Data Type (ADT)
* Queue() creates a new queue that is empty.
  It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue.
  It needs the item and returns nothing.
* dequeue() removes the front item from the queue.
  It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty.
  It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue.
  It needs no parameters and returns an integer.
* peek() returns the front element of the queue.
"""
import unittest


class AbstractQueue:
    def __init__(self):
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size


class ArrayQueue(AbstractQueue):
    def __init__(self, capacity=10):
        """
        Initialize python List with capacity of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        AbstractQueue.__init__(self)
        self._array = [None] * capacity
        self._front = 0
        self._rear = 0

    def enqueue(self, value):
        if self._rear == len(self._array):
            self.expand()
        self._array[self._rear] = value
        self._rear += 1
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._array[self._front]
        self._array[self._front] = None
        self._front += 1
        self._size -= 1
        return value

    def expand(self):
        """expands size of the array.
         Time Complexity: O(n)
        """
        self._array += [None] * len(self._array)

    def peek(self):
        """returns the front element of queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]

    def __iter__(self):
        probe = self._front
        while True:
            if probe == self._rear:
                raise StopIteration
            yield self._array[probe]
            probe += 1


class QueueNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue(AbstractQueue):
    def __init__(self):
        AbstractQueue.__init__(self)
        self._front = None
        self._rear = None

    def enqueue(self, value):
        node = QueueNode(value)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._front.value
        if self._front is self._rear:
            self._front = None
            self._rear = None
        else:
            self._front = self._front.next
        self._size -= 1
        return value

    def peek(self):
        """returns the front element of queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.value

    def __iter__(self):
        probe = self._front
        while True:
            if probe is None:
                raise StopIteration
            yield probe.value
            probe = probe.next


# TODO
class HeapPriorityQueue(AbstractQueue):
    pass


class TestSuite(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
