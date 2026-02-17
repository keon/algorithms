"""
Switch Pairs

Switch successive pairs of values in a stack starting from the bottom.
If there is an odd number of values, the top element is not moved.
Two approaches: one using an auxiliary stack, one using an auxiliary queue.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

import collections


def first_switch_pairs(stack: list[int]) -> list[int]:
    """Switch successive pairs using an auxiliary stack.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        The stack with successive pairs swapped.

    Examples:
        >>> first_switch_pairs([3, 8, 17, 9, 1, 10])
        [8, 3, 9, 17, 10, 1]
    """
    storage_stack: list[int] = []
    for _ in range(len(stack)):
        storage_stack.append(stack.pop())
    for _ in range(len(storage_stack)):
        if len(storage_stack) == 0:
            break
        first = storage_stack.pop()
        if len(storage_stack) == 0:
            stack.append(first)
            break
        second = storage_stack.pop()
        stack.append(second)
        stack.append(first)
    return stack


def second_switch_pairs(stack: list[int]) -> list[int]:
    """Switch successive pairs using an auxiliary queue.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        The stack with successive pairs swapped.

    Examples:
        >>> second_switch_pairs([3, 8, 17, 9, 1, 10])
        [8, 3, 9, 17, 10, 1]
    """
    queue: collections.deque[int] = collections.deque()
    for _ in range(len(stack)):
        queue.append(stack.pop())
    for _ in range(len(queue)):
        stack.append(queue.pop())
    for _ in range(len(stack)):
        queue.append(stack.pop())
    for _ in range(len(queue)):
        if len(queue) == 0:
            break
        first = queue.pop()
        if len(queue) == 0:
            stack.append(first)
            break
        second = queue.pop()
        stack.append(second)
        stack.append(first)

    return stack
