"""
Count Ones (Hamming Weight)

Count the number of 1-bits in the binary representation of an unsigned
integer using Brian Kernighan's algorithm.

Reference: https://en.wikipedia.org/wiki/Hamming_weight

Complexity:
    Time:  O(k) where k is the number of set bits
    Space: O(1) iterative / O(k) recursive (call stack)
"""

from __future__ import annotations


def count_ones_recur(number: int) -> int:
    """Count set bits using Brian Kernighan's algorithm (recursive).

    Args:
        number: A non-negative integer.

    Returns:
        The number of 1-bits in the binary representation.

    Examples:
        >>> count_ones_recur(8)
        1
        >>> count_ones_recur(63)
        6
    """
    if not number:
        return 0
    return 1 + count_ones_recur(number & (number - 1))


def count_ones_iter(number: int) -> int:
    """Count set bits using Brian Kernighan's algorithm (iterative).

    Args:
        number: A non-negative integer.

    Returns:
        The number of 1-bits in the binary representation.

    Examples:
        >>> count_ones_iter(8)
        1
        >>> count_ones_iter(63)
        6
    """
    count = 0
    while number:
        number &= (number - 1)
        count += 1
    return count
