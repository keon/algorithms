"""
Queue Abstract Data Type

Implementations of the queue ADT using both a fixed-size array and a
linked list. Both support enqueue, dequeue, peek, is_empty, len, and iter.

Reference: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

Complexity:
    Time:  O(1) for enqueue/dequeue/peek (amortized for ArrayQueue)
    Space: O(n)
"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Iterator


class AbstractQueue(metaclass=ABCMeta):
    """Abstract base class for queue implementations."""

    def __init__(self) -> None:
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            True if the queue has no elements.
        """
        return self._size == 0

    @abstractmethod
    def enqueue(self, value: object) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> object:
        pass

    @abstractmethod
    def peek(self) -> object:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[object]:
        pass


class ArrayQueue(AbstractQueue):
    """Queue implemented with a dynamic array.

    Examples:
        >>> q = ArrayQueue()
        >>> q.enqueue(1)
        >>> q.dequeue()
        1
    """

    def __init__(self, capacity: int = 10) -> None:
        """Initialize with a fixed-capacity array.

        Args:
            capacity: Initial capacity of the underlying array.
        """
        super().__init__()
        self._array: list[object | None] = [None] * capacity
        self._front = 0
        self._rear = 0

    def __iter__(self) -> Iterator[object]:
        probe = self._front
        while True:
            if probe == self._rear:
                return
            yield self._array[probe]
            probe += 1

    def enqueue(self, value: object) -> None:
        """Add an item to the rear of the queue.

        Args:
            value: The value to enqueue.
        """
        if self._rear == len(self._array):
            self._expand()
        self._array[self._rear] = value
        self._rear += 1
        self._size += 1

    def dequeue(self) -> object:
        """Remove and return the front item.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._array[self._front]
        self._array[self._front] = None
        self._front += 1
        self._size -= 1
        return value

    def peek(self) -> object:
        """Return the front element without removing it.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._array[self._front]

    def _expand(self) -> None:
        """Double the size of the underlying array."""
        self._array += [None] * len(self._array)


class QueueNode:
    """A single node in a linked-list-based queue."""

    def __init__(self, value: object) -> None:
        self.value = value
        self.next: QueueNode | None = None


class LinkedListQueue(AbstractQueue):
    """Queue implemented with a singly linked list.

    Examples:
        >>> q = LinkedListQueue()
        >>> q.enqueue(1)
        >>> q.dequeue()
        1
    """

    def __init__(self) -> None:
        super().__init__()
        self._front: QueueNode | None = None
        self._rear: QueueNode | None = None

    def __iter__(self) -> Iterator[object]:
        probe = self._front
        while True:
            if probe is None:
                return
            yield probe.value
            probe = probe.next

    def enqueue(self, value: object) -> None:
        """Add an item to the rear of the queue.

        Args:
            value: The value to enqueue.
        """
        node = QueueNode(value)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self) -> object:
        """Remove and return the front item.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
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

    def peek(self) -> object:
        """Return the front element without removing it.

        Returns:
            The front element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.value
