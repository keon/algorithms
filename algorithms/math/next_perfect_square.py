"""
Next Perfect Square

Given a number, find the next perfect square if the input is itself a perfect
square. Otherwise, return -1.

Reference: https://en.wikipedia.org/wiki/Square_number

Uses integer square roots and exact square verification. The arithmetic cost
depends on the bit length of the input.
"""

from __future__ import annotations

from math import isqrt


def find_next_square(sq: int | float) -> int:
    """Find the next perfect square after sq.

    Args:
        sq: A non-negative finite number to check.

    Returns:
        The next perfect square if sq is a perfect square, otherwise -1.

    Examples:
        >>> find_next_square(121)
        144
        >>> find_next_square(10)
        -1
    """
    root = isqrt(int(sq))
    if root * root == sq:
        return (root + 1) ** 2
    return -1


def find_next_square2(sq: int | float) -> int:
    """Find the next perfect square using exact square verification.

    Args:
        sq: A non-negative finite number to check.

    Returns:
        The next perfect square if sq is a perfect square, otherwise -1.

    Examples:
        >>> find_next_square2(121)
        144
        >>> find_next_square2(10)
        -1
    """
    root = isqrt(int(sq))
    return (root + 1) ** 2 if root * root == sq else -1
