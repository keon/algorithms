"""
Binary Gap

Given a positive integer N, find and return the longest distance between two
consecutive 1-bits in the binary representation of N. If there are not two
consecutive 1-bits, return 0.

Reference: https://en.wikipedia.org/wiki/Hamming_distance

Complexity:
    Time:  O(log n) where n is the input integer
    Space: O(1)
"""

from __future__ import annotations


def binary_gap(number: int) -> int:
    """Find the longest distance between consecutive 1-bits in binary.

    Args:
        number: A positive integer to examine.

    Returns:
        The longest gap between consecutive 1-bits, or 0 if fewer
        than two 1-bits exist.

    Examples:
        >>> binary_gap(22)
        2
        >>> binary_gap(8)
        0
    """
    last_one_position = None
    longest_gap = 0
    index = 0
    while number != 0:
        if number & 1:
            if last_one_position is not None:
                longest_gap = max(longest_gap, index - last_one_position)
            last_one_position = index
        index += 1
        number >>= 1
    return longest_gap
