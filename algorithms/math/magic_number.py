"""
Magic Number

A magic number is a number where recursively summing its digits eventually
yields 1. For example, 199 -> 1+9+9=19 -> 1+9=10 -> 1+0=1.

Reference: https://en.wikipedia.org/wiki/Digital_root

Complexity:
    Time:  O(log n) amortized
    Space: O(1)
"""

from __future__ import annotations


def magic_number(n: int) -> bool:
    """Check if n is a magic number (digital root equals 1).

    Args:
        n: The integer to check.

    Returns:
        True if the digital root of n is 1, False otherwise.

    Examples:
        >>> magic_number(1234)
        True
        >>> magic_number(111)
        False
    """
    total_sum = 0

    while n > 0 or total_sum > 9:
        if n == 0:
            n = total_sum
            total_sum = 0
        total_sum += n % 10
        n //= 10

    return total_sum == 1
