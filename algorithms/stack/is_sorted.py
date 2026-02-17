"""
Is Sorted

Check whether a stack is sorted in ascending order from bottom to top
using a single auxiliary stack.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def is_sorted(stack: list[int]) -> bool:
    """Check if a stack is sorted in ascending order (bottom to top).

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        True if sorted in ascending order, False otherwise.

    Examples:
        >>> is_sorted([1, 2, 3, 4, 5, 6])
        True
        >>> is_sorted([6, 3, 5, 1, 2, 4])
        False
    """
    storage_stack: list[int] = []
    for _ in range(len(stack)):
        if len(stack) == 0:
            break
        first_val = stack.pop()
        if len(stack) == 0:
            break
        second_val = stack.pop()
        if first_val < second_val:
            return False
        storage_stack.append(first_val)
        stack.append(second_val)

    for _ in range(len(storage_stack)):
        stack.append(storage_stack.pop())

    return True
