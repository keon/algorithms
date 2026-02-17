"""
Modular Multiplicative Inverse

Find x such that a * x = 1 (mod m) using the Extended Euclidean Algorithm.
Requires a and m to be coprime.

Reference: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

Complexity:
    Time:  O(log(min(a, m)))
    Space: O(1)
"""

from __future__ import annotations


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Compute the extended GCD of two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        A tuple (s, t, g) where a * s + b * t = g = gcd(a, b).
    """
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r


def modular_inverse(a: int, m: int) -> int:
    """Find x such that a * x = 1 (mod m).

    Args:
        a: The integer to find the inverse of.
        m: The modulus (must be coprime with a).

    Returns:
        The modular multiplicative inverse of a modulo m.

    Raises:
        ValueError: If a and m are not coprime.

    Examples:
        >>> modular_inverse(2, 19)
        10
    """
    s, _, g = _extended_gcd(a, m)
    if g != 1:
        raise ValueError("a and m must be coprime")
    return s % m
