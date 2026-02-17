"""
Primality Test

Check whether a given integer is prime using trial division with 6k +/- 1
optimization.

Reference: https://en.wikipedia.org/wiki/Primality_test

Complexity:
    Time:  O(sqrt(n))
    Space: O(1)
"""

from __future__ import annotations


def prime_check(n: int) -> bool:
    """Check whether n is a prime number.

    Args:
        n: The integer to test.

    Returns:
        True if n is prime, False otherwise.

    Examples:
        >>> prime_check(7)
        True
        >>> prime_check(4)
        False
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True
