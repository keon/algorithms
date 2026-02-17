"""
Elias Gamma and Delta Coding

Universal codes for encoding positive integers. Elias gamma code uses a unary
prefix followed by a binary suffix. Elias delta code nests gamma coding for
the length prefix. Both were developed by Peter Elias.

Reference: https://en.wikipedia.org/wiki/Elias_gamma_coding

Complexity:
    Time:  O(log n) per encoded integer
    Space: O(log n)
"""

from __future__ import annotations

from math import log


def _log2(x: int | float) -> float:
    """Compute log base 2.

    Args:
        x: A positive number.

    Returns:
        The base-2 logarithm of x.
    """
    return log(x, 2)


def _binary(x: int, length: int = 1) -> str:
    """Return the binary representation of x zero-padded to length digits.

    Args:
        x: A non-negative integer.
        length: Minimum number of binary digits.

    Returns:
        A binary string.
    """
    fmt = "{0:0%db}" % length
    return fmt.format(x)


def _unary(x: int) -> str:
    """Return the unary representation of x.

    Args:
        x: A positive integer.

    Returns:
        A unary-coded string (x-1 ones followed by a zero).
    """
    return (x - 1) * "1" + "0"


def _elias_generic(
    length_encoding: callable,
    x: int,
) -> str:
    """Generic Elias encoding using a pluggable length-encoding function.

    Args:
        length_encoding: A function to encode the length prefix.
        x: A non-negative integer to encode.

    Returns:
        The Elias-coded bit string.
    """
    if x == 0:
        return "0"

    first_part = 1 + int(_log2(x))
    remainder = x - 2 ** int(_log2(x))
    bit_count = int(_log2(x))

    return length_encoding(first_part) + _binary(remainder, bit_count)


def elias_gamma(x: int) -> str:
    """Encode a positive integer using Elias gamma coding.

    Args:
        x: A non-negative integer.

    Returns:
        The Elias gamma coded bit string.

    Examples:
        >>> elias_gamma(1)
        '0'
        >>> elias_gamma(5)
        '00101'
    """
    return _elias_generic(_unary, x)


def elias_delta(x: int) -> str:
    """Encode a positive integer using Elias delta coding.

    Args:
        x: A non-negative integer.

    Returns:
        The Elias delta coded bit string.

    Examples:
        >>> elias_delta(1)
        '0'
        >>> elias_delta(5)
        '01101'
    """
    return _elias_generic(elias_gamma, x)
