"""
Minimum Perfect Squares Sum

Determine the minimum number of perfect squares that sum to a given integer.
By Lagrange's four-square theorem, the answer is always between 1 and 4.

Reference: https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem

Complexity:
    Time:  O(sqrt(n))
    Space: O(1)
"""

from __future__ import annotations

import math


def num_perfect_squares(number: int) -> int:
    """Find the minimum count of perfect squares that sum to number.

    Args:
        number: A positive integer.

    Returns:
        An integer between 1 and 4 representing the minimum count.

    Examples:
        >>> num_perfect_squares(9)
        1
        >>> num_perfect_squares(10)
        2
        >>> num_perfect_squares(12)
        3
        >>> num_perfect_squares(31)
        4
    """
    if int(math.sqrt(number)) ** 2 == number:
        return 1

    while number > 0 and number % 4 == 0:
        number /= 4

    if number % 8 == 7:
        return 4

    for i in range(1, int(math.sqrt(number)) + 1):
        if int(math.sqrt(number - i**2)) ** 2 == number - i**2:
            return 2

    return 3
