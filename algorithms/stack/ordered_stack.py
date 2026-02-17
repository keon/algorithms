"""
Ordered Stack

A stack that maintains elements in sorted order, with the highest value
at the top and the lowest at the bottom. Push operations preserve the
ordering invariant.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n) for push, O(1) for pop/peek
    Space: O(n)
"""

from __future__ import annotations


class OrderedStack:
    """A stack that keeps elements in ascending order (bottom to top).

    Examples:
        >>> s = OrderedStack()
        >>> s.push(3)
        >>> s.push(1)
        >>> s.push(2)
        >>> s.pop()
        3
    """

    def __init__(self) -> None:
        """Initialize an empty ordered stack."""
        self.items: list[int] = []

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if the stack has no elements.
        """
        return self.items == []

    def _push_direct(self, item: int) -> None:
        """Append an item without enforcing order.

        Args:
            item: The value to append.
        """
        self.items.append(item)

    def push(self, item: int) -> None:
        """Push an item while maintaining sorted order.

        Args:
            item: The value to push.
        """
        temp_stack = OrderedStack()
        if self.is_empty() or item > self.peek():
            self._push_direct(item)
        else:
            while item < self.peek() and not self.is_empty():
                temp_stack._push_direct(self.pop())
            self._push_direct(item)
            while not temp_stack.is_empty():
                self._push_direct(temp_stack.pop())

    def pop(self) -> int:
        """Remove and return the top element.

        Returns:
            The top (largest) element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> int:
        """Return the top element without removing it.

        Returns:
            The top (largest) element.
        """
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            The stack size.
        """
        return len(self.items)
