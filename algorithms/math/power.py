"""
Binary Exponentiation

Compute a^n efficiently using binary exponentiation (exponentiation by
squaring), with optional modular arithmetic.

Reference: https://en.wikipedia.org/wiki/Exponentiation_by_squaring

Complexity:
    Time:  O(log n)
    Space: O(1) iterative, O(log n) recursive
"""

from __future__ import annotations


def power(a: int, n: int, mod: int | None = None) -> int:
    """Compute a^n iteratively using binary exponentiation.

    Args:
        a: The base.
        n: The exponent.
        mod: Optional modulus for modular exponentiation.

    Returns:
        a^n, or a^n % mod if mod is specified.

    Examples:
        >>> power(2, 3)
        8
        >>> power(10, 3, 5)
        0
    """
    ans = 1
    while n:
        if n & 1:
            ans = ans * a
        a = a * a
        if mod:
            ans %= mod
            a %= mod
        n >>= 1
    return ans


def power_recur(a: int, n: int, mod: int | None = None) -> int:
    """Compute a^n recursively using binary exponentiation.

    Args:
        a: The base.
        n: The exponent.
        mod: Optional modulus for modular exponentiation.

    Returns:
        a^n, or a^n % mod if mod is specified.

    Examples:
        >>> power_recur(2, 3)
        8
    """
    if n == 0:
        ans = 1
    elif n == 1:
        ans = a
    else:
        ans = power_recur(a, n // 2, mod)
        ans = ans * ans
        if n % 2:
            ans = ans * a
    if mod:
        ans %= mod
    return ans
