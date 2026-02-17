"""
Extended Euclidean Algorithm

Find coefficients s and t (Bezout's identity) such that:
num1 * s + num2 * t = gcd(num1, num2).

Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

Complexity:
    Time:  O(log(min(num1, num2)))
    Space: O(1)
"""

from __future__ import annotations


def extended_gcd(num1: int, num2: int) -> tuple[int, int, int]:
    """Compute the extended GCD of two integers.

    Args:
        num1: First integer.
        num2: Second integer.

    Returns:
        A tuple (s, t, g) where num1 * s + num2 * t = g = gcd(num1, num2).

    Examples:
        >>> extended_gcd(8, 2)
        (0, 1, 2)
        >>> extended_gcd(13, 17)
        (0, 1, 17)
    """
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = num1, num2

    while r != 0:
        quotient = old_r / r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r
