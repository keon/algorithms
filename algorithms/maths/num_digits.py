"""
Number of Digits

Count the number of digits in an integer using logarithmic computation
for O(1) time complexity.

Reference: https://en.wikipedia.org/wiki/Logarithm

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations

import math


def num_digits(n: int) -> int:
    """Count the number of digits in an integer.

    Args:
        n: An integer (negative values use their absolute value).

    Returns:
        The number of digits in n.

    Examples:
        >>> num_digits(12)
        2
        >>> num_digits(0)
        1
        >>> num_digits(-254)
        3
    """
    n = abs(n)
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
