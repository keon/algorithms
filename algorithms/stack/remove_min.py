"""
Remove Min from Stack

Remove the smallest value from a stack, preserving the relative order
of the remaining elements.

Reference: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def remove_min(stack: list[int]) -> list[int]:
    """Remove the minimum value from the stack.

    Args:
        stack: A list representing a stack (bottom to top).

    Returns:
        The stack with the minimum value removed.

    Examples:
        >>> remove_min([2, 8, 3, -6, 7, 3])
        [2, 8, 3, 7, 3]
    """
    storage_stack: list[int] = []
    if len(stack) == 0:
        return stack
    minimum = stack.pop()
    stack.append(minimum)
    for _ in range(len(stack)):
        val = stack.pop()
        if val <= minimum:
            minimum = val
        storage_stack.append(val)
    for _ in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != minimum:
            stack.append(val)
    return stack
