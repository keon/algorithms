"""
Find the Nth Digit

Find the nth digit in the infinite sequence 1, 2, 3, ..., 9, 10, 11, 12, ...
by determining which number contains it and extracting the specific digit.

Reference: https://en.wikipedia.org/wiki/Positional_notation

Complexity:
    Time:  O(log n)
    Space: O(log n) for string conversion
"""

from __future__ import annotations


def find_nth_digit(n: int) -> int:
    """Find the nth digit in the sequence of natural numbers.

    Args:
        n: The 1-based position of the digit to find.

    Returns:
        The digit at position n.

    Examples:
        >>> find_nth_digit(11)
        0
    """
    length = 1
    count = 9
    start = 1
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    start += (n - 1) / length
    s = str(start)
    return int(s[(n - 1) % length])
