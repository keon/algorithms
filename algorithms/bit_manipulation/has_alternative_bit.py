"""
Has Alternating Bits

Check whether a positive integer has alternating bits, meaning no two
adjacent bits share the same value.

Reference: https://en.wikipedia.org/wiki/Bit_manipulation

Complexity:
    has_alternative_bit:      O(number of bits)
    has_alternative_bit_fast: O(1)
"""

from __future__ import annotations


def has_alternative_bit(number: int) -> bool:
    """Check for alternating bits by scanning each pair of adjacent bits.

    Args:
        number: A positive integer to check.

    Returns:
        True if every pair of adjacent bits differs, False otherwise.

    Examples:
        >>> has_alternative_bit(5)
        True
        >>> has_alternative_bit(7)
        False
    """
    first_bit = 0
    second_bit = 0
    while number:
        first_bit = number & 1
        if number >> 1:
            second_bit = (number >> 1) & 1
            if not first_bit ^ second_bit:
                return False
        else:
            return True
        number >>= 1
    return True


def has_alternative_bit_fast(number: int) -> bool:
    """Check for alternating bits using O(1) bitmask arithmetic.

    Args:
        number: A positive integer to check.

    Returns:
        True if every pair of adjacent bits differs, False otherwise.

    Examples:
        >>> has_alternative_bit_fast(5)
        True
        >>> has_alternative_bit_fast(7)
        False
    """
    mask_even_bits = int("aaaaaaaa", 16)  # ...10101010
    mask_odd_bits = int("55555555", 16)  # ...01010101
    return mask_even_bits == (number + (number ^ mask_even_bits)) or mask_odd_bits == (
        number + (number ^ mask_odd_bits)
    )
