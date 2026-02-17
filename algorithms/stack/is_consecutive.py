"""
Is Consecutive

Check whether a stack contains a sequence of consecutive integers
starting from the bottom. Two approaches are provided: one using an
auxiliary stack, and one using an auxiliary queue.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

import collections


def first_is_consecutive(stack: list[int]) -> bool:
    """Check if a stack has consecutive integers using an auxiliary stack.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        True if the values are consecutive from bottom to top.

    Examples:
        >>> first_is_consecutive([3, 4, 5, 6, 7])
        True
        >>> first_is_consecutive([3, 4, 6, 7])
        False
    """
    storage_stack: list[int] = []
    for _ in range(len(stack)):
        first_value = stack.pop()
        if len(stack) == 0:
            return True
        second_value = stack.pop()
        if first_value - second_value != 1:
            return False
        stack.append(second_value)
        storage_stack.append(first_value)

    for _ in range(len(storage_stack)):
        stack.append(storage_stack.pop())
    return True


def second_is_consecutive(stack: list[int]) -> bool:
    """Check if a stack has consecutive integers using an auxiliary queue.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        True if the values are consecutive from bottom to top.

    Examples:
        >>> second_is_consecutive([3, 4, 5, 6, 7])
        True
        >>> second_is_consecutive([3, 4, 6, 7])
        False
    """
    queue: collections.deque[int] = collections.deque()
    for _ in range(len(stack)):
        first_value = stack.pop()
        if len(stack) == 0:
            return True
        second_value = stack.pop()
        if first_value - second_value != 1:
            return False
        stack.append(second_value)
        queue.append(first_value)

    for _ in range(len(queue)):
        stack.append(queue.pop())
    for _ in range(len(stack)):
        queue.append(stack.pop())
    for _ in range(len(queue)):
        stack.append(queue.pop())

    return True
