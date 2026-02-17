"""
Greatest Common Divisor and Least Common Multiple

Compute the GCD and LCM of two integers using Euclid's algorithm and
a bitwise variant.

Reference: https://en.wikipedia.org/wiki/Euclidean_algorithm

Complexity:
    Time:  O(log(min(a, b))) for gcd, O(log(min(a, b))) for lcm
    Space: O(1)
"""

from __future__ import annotations


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor using Euclid's algorithm.

    Args:
        a: First integer (non-zero).
        b: Second integer (non-zero).

    Returns:
        The greatest common divisor of a and b.

    Raises:
        ValueError: If inputs are not integers or either is zero.

    Examples:
        >>> gcd(8, 12)
        4
        >>> gcd(13, 17)
        1
    """
    a_int = isinstance(a, int)
    b_int = isinstance(b, int)
    a = abs(a)
    b = abs(b)
    if not (a_int or b_int):
        raise ValueError("Input arguments are not integers")

    if (a == 0) or (b == 0):
        raise ValueError("One or more input arguments equals zero")

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Compute the lowest common multiple of two integers.

    Args:
        a: First integer (non-zero).
        b: Second integer (non-zero).

    Returns:
        The lowest common multiple of a and b.

    Examples:
        >>> lcm(8, 12)
        24
    """
    return abs(a) * abs(b) / gcd(a, b)


def trailing_zero(x: int) -> int:
    """Count the number of trailing zeros in the binary representation.

    Args:
        x: A positive integer.

    Returns:
        Number of trailing zero bits.

    Examples:
        >>> trailing_zero(34)
        1
        >>> trailing_zero(40)
        3
    """
    count = 0
    while x and not x & 1:
        count += 1
        x >>= 1
    return count


def gcd_bit(a: int, b: int) -> int:
    """Compute GCD using the binary (Stein's) algorithm.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        The greatest common divisor of a and b.

    Examples:
        >>> gcd_bit(8, 12)
        4
    """
    tza = trailing_zero(a)
    tzb = trailing_zero(b)
    a >>= tza
    b >>= tzb
    while b:
        if a < b:
            a, b = b, a
        a -= b
        a >>= trailing_zero(a)
    return a << min(tza, tzb)
