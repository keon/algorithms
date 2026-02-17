r"""
Binary Heap

A min heap is a complete binary tree where each node is smaller than
its children. The root is the minimum element. Uses an array
representation with index 0 as a sentinel.

Reference: https://en.wikipedia.org/wiki/Binary_heap

Complexity:
    Time:  O(log n) for insert and remove_min
    Space: O(n)
"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    """Abstract base class for binary heap implementations."""

    def __init__(self) -> None:
        """Initialize the abstract heap."""

    @abstractmethod
    def perc_up(self, index: int) -> None:
        """Percolate element up to restore heap property.

        Args:
            index: Index of the element to percolate up.
        """

    @abstractmethod
    def insert(self, val: int) -> None:
        """Insert a value into the heap.

        Args:
            val: The value to insert.
        """

    @abstractmethod
    def perc_down(self, index: int) -> None:
        """Percolate element down to restore heap property.

        Args:
            index: Index of the element to percolate down.
        """

    @abstractmethod
    def min_child(self, index: int) -> int:
        """Return the index of the smaller child.

        Args:
            index: Index of the parent node.

        Returns:
            Index of the smaller child.
        """

    @abstractmethod
    def remove_min(self) -> int:
        """Remove and return the minimum element.

        Returns:
            The minimum value in the heap.
        """


class BinaryHeap(AbstractHeap):
    """Min binary heap using array representation.

    Examples:
        >>> heap = BinaryHeap()
        >>> heap.insert(5)
        >>> heap.insert(3)
        >>> heap.remove_min()
        3
    """

    def __init__(self) -> None:
        """Initialize the binary heap with a sentinel at index 0."""
        self.current_size: int = 0
        self.heap: list[int] = [0]

    def perc_up(self, index: int) -> None:
        """Percolate element up to maintain the min-heap invariant.

        Args:
            index: Index of the element to percolate up.
        """
        while index // 2 > 0:
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = (
                    self.heap[index // 2],
                    self.heap[index],
                )
            index = index // 2

    def insert(self, val: int) -> None:
        """Insert a value into the heap.

        Args:
            val: The value to insert.
        """
        self.heap.append(val)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def min_child(self, index: int) -> int:
        """Return the index of the smaller child of a parent node.

        Args:
            index: Index of the parent node.

        Returns:
            Index of the smaller child.
        """
        if 2 * index + 1 > self.current_size:
            return 2 * index
        if self.heap[2 * index] > self.heap[2 * index + 1]:
            return 2 * index + 1
        return 2 * index

    def perc_down(self, index: int) -> None:
        """Percolate element down to maintain the min-heap invariant.

        Args:
            index: Index of the element to percolate down.
        """
        while 2 * index < self.current_size:
            smaller_child = self.min_child(index)
            if self.heap[smaller_child] < self.heap[index]:
                self.heap[smaller_child], self.heap[index] = (
                    self.heap[index],
                    self.heap[smaller_child],
                )
            index = smaller_child

    def remove_min(self) -> int:
        """Remove and return the minimum element from the heap.

        Returns:
            The minimum value.
        """
        ret = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        self.perc_down(1)
        return ret
