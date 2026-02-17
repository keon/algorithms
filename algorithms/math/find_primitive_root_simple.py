"""
Primitive Root Finder

Find all primitive roots of a positive integer n. A primitive root modulo n
is an integer whose multiplicative order modulo n equals Euler's totient
of n.

Reference: https://en.wikipedia.org/wiki/Primitive_root_modulo_n

Complexity:
    Time:  O(n^2 log n)
    Space: O(n)
"""

from __future__ import annotations

import math


def _find_order(a: int, n: int) -> int:
    """Find the multiplicative order of a modulo n.

    Args:
        a: The base integer.
        n: The modulus.

    Returns:
        The smallest positive k where a^k = 1 (mod n), or -1 if none exists.
    """
    if (a == 1) & (n == 1):
        return 1
    if math.gcd(a, n) != 1:
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1


def _euler_totient(n: int) -> int:
    """Compute Euler's totient function phi(n).

    Args:
        n: A positive integer.

    Returns:
        The count of integers in [1, n] coprime to n.
    """
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result


def find_primitive_root(n: int) -> list[int]:
    """Find all primitive roots of n.

    Args:
        n: A positive integer.

    Returns:
        List of all primitive roots of n. Returns [0] for n=1, or an
        empty list if no primitive roots exist.

    Examples:
        >>> find_primitive_root(5)
        [2, 3]
        >>> find_primitive_root(1)
        [0]
    """
    if n == 1:
        return [0]
    phi = _euler_totient(n)
    p_root_list = []
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            order = _find_order(i, n)
            if order == phi:
                p_root_list.append(i)
    return p_root_list
