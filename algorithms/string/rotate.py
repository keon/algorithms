"""
Rotate String

Given a string and an integer k, return the string rotated by k positions
to the left. Two approaches are provided.

Reference: https://en.wikipedia.org/wiki/Circular_shift

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(n)
"""

from __future__ import annotations


def rotate(text: str, positions: int) -> str:
    """Rotate a string left by k positions using repeated string approach.

    Args:
        text: The string to rotate.
        positions: The number of positions to rotate left.

    Returns:
        The rotated string.

    Examples:
        >>> rotate("hello", 2)
        'llohe'
    """
    long_string = text * (positions // len(text) + 2)
    if positions <= len(text):
        return long_string[positions : positions + len(text)]
    else:
        return long_string[positions - len(text) : positions]


def rotate_alt(string: str, positions: int) -> str:
    """Rotate a string left by k positions using modular arithmetic.

    Args:
        string: The string to rotate.
        positions: The number of positions to rotate left.

    Returns:
        The rotated string.

    Examples:
        >>> rotate_alt("hello", 2)
        'llohe'
    """
    positions = positions % len(string)
    return string[positions:] + string[:positions]
