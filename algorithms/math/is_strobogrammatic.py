"""
Strobogrammatic Number Check

Determine whether a number (as a string) is strobogrammatic, meaning it
looks the same when rotated 180 degrees.

Reference: https://en.wikipedia.org/wiki/Strobogrammatic_number

Complexity:
    Time:  O(n) where n is the length of the number string
    Space: O(1) for is_strobogrammatic, O(n) for is_strobogrammatic2
"""

from __future__ import annotations


def is_strobogrammatic(num: str) -> bool:
    """Check if a number string is strobogrammatic using two pointers.

    Args:
        num: String representation of the number.

    Returns:
        True if num is strobogrammatic, False otherwise.

    Examples:
        >>> is_strobogrammatic("69")
        True
        >>> is_strobogrammatic("14")
        False
    """
    comb = "00 11 88 69 96"
    i = 0
    j = len(num) - 1
    while i <= j:
        if comb.find(num[i] + num[j]) == -1:
            return False
        i += 1
        j -= 1
    return True


def is_strobogrammatic2(num: str) -> bool:
    """Check if a number string is strobogrammatic using string reversal.

    Args:
        num: String representation of the number.

    Returns:
        True if num is strobogrammatic, False otherwise.

    Examples:
        >>> is_strobogrammatic2("69")
        True
        >>> is_strobogrammatic2("14")
        False
    """
    return num == num[::-1].replace('6', '#').replace('9', '6').replace('#', '9')
