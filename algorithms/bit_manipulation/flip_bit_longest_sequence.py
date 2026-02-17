"""
Flip Bit Longest Sequence

Given an integer, find the length of the longest sequence of 1-bits you
can create by flipping exactly one 0-bit to a 1-bit.

Reference: https://en.wikipedia.org/wiki/Bit_manipulation

Complexity:
    Time:  O(b) where b is the number of bits in the integer
    Space: O(1)
"""

from __future__ import annotations


def flip_bit_longest_seq(number: int) -> int:
    """Find the longest 1-bit run achievable by flipping a single 0-bit.

    Tracks the current run length and the previous run length to
    determine the best sequence that can be formed by bridging two
    runs with a single flipped bit.

    Args:
        number: A non-negative integer.

    Returns:
        The length of the longest sequence of 1-bits after one flip.

    Examples:
        >>> flip_bit_longest_seq(1775)
        8
        >>> flip_bit_longest_seq(0)
        1
    """
    current_length = 0
    previous_length = 0
    max_length = 0

    while number:
        if number & 1 == 1:
            current_length += 1
        elif number & 1 == 0:
            if number & 2 == 0:
                previous_length = 0
            else:
                previous_length = current_length
            current_length = 0

        max_length = max(max_length, previous_length + current_length)
        number >>= 1

    return max_length + 1
