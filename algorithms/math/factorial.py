"""
Factorial

Compute the factorial of a non-negative integer, with optional modular
arithmetic support.

Reference: https://en.wikipedia.org/wiki/Factorial

Complexity:
    Time:  O(n)
    Space: O(1) iterative, O(n) recursive
"""

from __future__ import annotations


def factorial(n: int, mod: int | None = None) -> int:
    """Calculate n! iteratively, optionally modulo mod.

    Args:
        n: A non-negative integer.
        mod: Optional positive integer modulus.

    Returns:
        n! or n! % mod if mod is provided.

    Raises:
        ValueError: If n is negative or mod is not a positive integer.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    result = 1
    if n == 0:
        return 1
    for i in range(2, n + 1):
        result *= i
        if mod:
            result %= mod
    return result


def factorial_recur(n: int, mod: int | None = None) -> int:
    """Calculate n! recursively, optionally modulo mod.

    Args:
        n: A non-negative integer.
        mod: Optional positive integer modulus.

    Returns:
        n! or n! % mod if mod is provided.

    Raises:
        ValueError: If n is negative or mod is not a positive integer.

    Examples:
        >>> factorial_recur(5)
        120
    """
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    if n == 0:
        return 1
    result = n * factorial(n - 1, mod)
    if mod:
        result %= mod
    return result
