"""
Move Zeros

Move all zeros in an array to the end while preserving the relative order
of the non-zero (and non-integer-zero) elements.

Reference: https://leetcode.com/problems/move-zeroes/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from typing import Any


def move_zeros(array: list[Any]) -> list[Any]:
    """Move all integer zeros to the end, preserving order of other elements.

    Boolean False is not treated as zero.

    Args:
        array: Input list with mixed types.

    Returns:
        New list with all integer 0s moved to the end.

    Examples:
        >>> move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])
        [False, 1, 1, 2, 1, 3, 'a', 0, 0]
    """
    result = []
    zeros = 0

    for element in array:
        if element == 0 and type(element) != bool:
            zeros += 1
        else:
            result.append(element)

    result.extend([0] * zeros)
    return result
