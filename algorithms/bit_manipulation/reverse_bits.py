"""
Reverse Bits

Reverse the bits of a 32-bit unsigned integer.

Reference: https://en.wikipedia.org/wiki/Bit_reversal

Complexity:
    Time:  O(1) -- always iterates exactly 32 times
    Space: O(1)
"""

from __future__ import annotations


def reverse_bits(number: int) -> int:
    """Reverse all 32 bits of an unsigned integer.

    Args:
        number: A 32-bit unsigned integer (0 to 2**32 - 1).

    Returns:
        The integer formed by reversing the bit order.

    Examples:
        >>> reverse_bits(43261596)
        964176192
        >>> reverse_bits(0)
        0
    """
    result = 0
    for _ in range(32):
        result = (result << 1) + (number & 1)
        number >>= 1
    return result
