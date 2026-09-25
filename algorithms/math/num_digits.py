"""
Number of Digits

Count decimal digits using a logarithmic estimate corrected with integer
comparisons. Floating-point rounding at powers of ten cannot change the result.

Reference: https://en.wikipedia.org/wiki/Logarithm

Complexity:
    Time:  Integer exponentiation and comparisons depend on the number of digits.
    Space: O(d) bits for d decimal digits (a constant number of integers).
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
    digits = int(math.log10(n)) + 1
    boundary = 10 ** (digits - 1)
    while n < boundary:
        digits -= 1
        boundary //= 10
    while n >= boundary * 10:
        digits += 1
        boundary *= 10
    return digits
