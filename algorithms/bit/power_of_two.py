"""
Power of Two

Determine whether a given integer is a power of two using bit manipulation.
A power of two has exactly one set bit, so ``n & (n - 1)`` clears that bit
and yields zero.

Reference: https://en.wikipedia.org/wiki/Power_of_two

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


def is_power_of_two(number: int) -> bool:
    """Check whether an integer is a power of two.

    Args:
        number: The integer to test.

    Returns:
        True if *number* is a positive power of two, False otherwise.

    Examples:
        >>> is_power_of_two(64)
        True
        >>> is_power_of_two(91)
        False
        >>> is_power_of_two(0)
        False
    """
    return number > 0 and not number & (number - 1)
