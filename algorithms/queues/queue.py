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
from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):

    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class ArrayQueue(AbstractQueue):

    def __init__(self, capacity=10):
        """
        Initialize python List with capacity of 10 or user given input.
        Python List type is a dynamic array, so we have to restrict its
        dynamic nature to make it work like a static array.
        """
        super().__init__()
        self._array = [None] * capacity
        self._front = 0
        self._rear = 0

    def __iter__(self):
        probe = self._front
        while True:
            if probe == self._rear:
                return
            yield self._array[probe]
            probe += 1

    def enqueue(self, value):
        if self._rear == len(self._array):
            self._expand()
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

    def peek(self):
        """returns the front element of queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]

    def _expand(self):
        """expands size of the array.
         Time Complexity: O(n)
        """
        self._array += [None] * len(self._array)


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue(AbstractQueue):

    def __init__(self):
        super().__init__()
        self._front = None
        self._rear = None

    def __iter__(self):
        probe = self._front
        while True:
            if probe is None:
                return
            yield probe.value
            probe = probe.next

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
