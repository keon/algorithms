"""
Multiplicative Order

Find the multiplicative order of a modulo n, which is the smallest positive
integer k such that a^k = 1 (mod n). Requires gcd(a, n) = 1.

Reference: https://en.wikipedia.org/wiki/Multiplicative_order

Complexity:
    Time:  O(n log n)
    Space: O(1)
"""

from __future__ import annotations

import math


def find_order(a: int, n: int) -> int:
    """Find the multiplicative order of a modulo n.

    Args:
        a: The base integer.
        n: The modulus.

    Returns:
        The smallest positive k where a^k = 1 (mod n), or -1 if a and n
        are not coprime.

    Examples:
        >>> find_order(3, 7)
        6
        >>> find_order(1, 1)
        1
    """
    if (a == 1) & (n == 1):
        return 1
    if math.gcd(a, n) != 1:
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1
