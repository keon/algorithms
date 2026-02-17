"""
Remove Bit

Remove a single bit at a specific position from an integer, shifting
higher bits down to fill the gap.

Reference: https://en.wikipedia.org/wiki/Bit_manipulation

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


def remove_bit(number: int, position: int) -> int:
    """Remove the bit at a specific position from an integer.

    Splits the number around *position*, shifts the upper part right
    by one to collapse the gap, and merges with the lower part.

    Args:
        number: The integer to modify.
        position: Zero-based index of the bit to remove.

    Returns:
        The resulting integer after removal.

    Examples:
        >>> remove_bit(21, 2)
        9
        >>> remove_bit(21, 4)
        5
        >>> remove_bit(21, 0)
        10
    """
    upper = number >> (position + 1)
    upper = upper << position
    lower = ((1 << position) - 1) & number
    return upper | lower
