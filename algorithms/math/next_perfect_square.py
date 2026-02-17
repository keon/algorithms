"""
Next Perfect Square

Given a number, find the next perfect square if the input is itself a perfect
square. Otherwise, return -1.

Reference: https://en.wikipedia.org/wiki/Square_number

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


def find_next_square(sq: float) -> float:
    """Find the next perfect square after sq.

    Args:
        sq: A non-negative number to check.

    Returns:
        The next perfect square if sq is a perfect square, otherwise -1.

    Examples:
        >>> find_next_square(121)
        144
        >>> find_next_square(10)
        -1
    """
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1


def find_next_square2(sq: float) -> float:
    """Find the next perfect square using modulo check.

    Args:
        sq: A non-negative number to check.

    Returns:
        The next perfect square if sq is a perfect square, otherwise -1.

    Examples:
        >>> find_next_square2(121)
        144
        >>> find_next_square2(10)
        -1
    """
    root = sq ** 0.5
    return -1 if root % 1 else (root + 1) ** 2
