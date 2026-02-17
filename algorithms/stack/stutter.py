"""
Stutter

Replace every value in a stack with two occurrences of that value.
Two approaches: one using an auxiliary stack, one using an auxiliary queue.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

import collections


def first_stutter(stack: list[int]) -> list[int]:
    """Stutter a stack using an auxiliary stack.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        The stack with each value duplicated.

    Examples:
        >>> first_stutter([3, 7, 1, 14, 9])
        [3, 3, 7, 7, 1, 1, 14, 14, 9, 9]
    """
    storage_stack: list[int] = []
    for _ in range(len(stack)):
        storage_stack.append(stack.pop())
    for _ in range(len(storage_stack)):
        val = storage_stack.pop()
        stack.append(val)
        stack.append(val)

    return stack


def second_stutter(stack: list[int]) -> list[int]:
    """Stutter a stack using an auxiliary queue.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        The stack with each value duplicated.

    Examples:
        >>> second_stutter([3, 7, 1, 14, 9])
        [3, 3, 7, 7, 1, 1, 14, 14, 9, 9]
    """
    queue: collections.deque[int] = collections.deque()
    for _ in range(len(stack)):
        queue.append(stack.pop())
    for _ in range(len(queue)):
        stack.append(queue.pop())
    for _ in range(len(stack)):
        queue.append(stack.pop())
    for _ in range(len(queue)):
        val = queue.pop()
        stack.append(val)
        stack.append(val)

    return stack
