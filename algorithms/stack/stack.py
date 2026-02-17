"""
Stack Abstract Data Type

Implementations of the stack ADT using both a fixed-size array and a
linked list. Both support push, pop, peek, is_empty, len, iter, and str.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(1) for push/pop/peek (amortized for ArrayStack)
    Space: O(n)
"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Iterator


class AbstractStack(metaclass=ABCMeta):
    """Abstract base class for stack implementations."""

    def __init__(self) -> None:
        self._top = -1

    def __len__(self) -> int:
        return self._top + 1

    def __str__(self) -> str:
        result = " ".join(map(str, self))
        return "Top-> " + result

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if the stack has no elements.
        """
        return self._top == -1

    @abstractmethod
    def __iter__(self) -> Iterator[object]:
        pass

    @abstractmethod
    def push(self, value: object) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def peek(self) -> object:
        pass


class ArrayStack(AbstractStack):
    """Stack implemented with a dynamic array.

    Examples:
        >>> s = ArrayStack()
        >>> s.push(1)
        >>> s.pop()
        1
    """

    def __init__(self, size: int = 10) -> None:
        """Initialize with a fixed-size array.

        Args:
            size: Initial capacity of the underlying array.
        """
        super().__init__()
        self._array: list[object | None] = [None] * size

    def __iter__(self) -> Iterator[object]:
        probe = self._top
        while True:
            if probe == -1:
                return
            yield self._array[probe]
            probe -= 1

    def push(self, value: object) -> None:
        """Push a value onto the stack.

        Args:
            value: The value to push.
        """
        self._top += 1
        if self._top == len(self._array):
            self._expand()
        self._array[self._top] = value

    def pop(self) -> object:
        """Remove and return the top element.

        Returns:
            The top element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self._array[self._top]
        self._top -= 1
        return value

    def peek(self) -> object:
        """Return the top element without removing it.

        Returns:
            The top element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._array[self._top]

    def _expand(self) -> None:
        """Double the size of the underlying array."""
        self._array += [None] * len(self._array)


class StackNode:
    """A single node in a linked-list-based stack."""

    def __init__(self, value: object) -> None:
        self.value = value
        self.next: StackNode | None = None


class LinkedListStack(AbstractStack):
    """Stack implemented with a singly linked list.

    Examples:
        >>> s = LinkedListStack()
        >>> s.push(1)
        >>> s.pop()
        1
    """

    def __init__(self) -> None:
        super().__init__()
        self.head: StackNode | None = None

    def __iter__(self) -> Iterator[object]:
        probe = self.head
        while True:
            if probe is None:
                return
            yield probe.value
            probe = probe.next

    def push(self, value: object) -> None:
        """Push a value onto the stack.

        Args:
            value: The value to push.
        """
        node = StackNode(value)
        node.next = self.head
        self.head = node
        self._top += 1

    def pop(self) -> object:
        """Remove and return the top element.

        Returns:
            The top element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        self._top -= 1
        return value

    def peek(self) -> object:
        """Return the top element without removing it.

        Returns:
            The top element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.value
