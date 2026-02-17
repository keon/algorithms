"""
Count Binary Substrings

Count the number of non-empty contiguous substrings that have the same number
of 0s and 1s, where all 0s and all 1s are grouped consecutively.

Reference: https://leetcode.com/problems/count-binary-substrings/

Complexity:
    Time:  O(n) where n is the length of the string
    Space: O(1)
"""

from __future__ import annotations


def count_binary_substring(text: str) -> int:
    """Count substrings with equal consecutive 0s and 1s.

    Args:
        text: A binary string consisting of '0' and '1' characters.

    Returns:
        The number of valid binary substrings.

    Examples:
        >>> count_binary_substring("00110011")
        6
    """
    current = 1
    previous = 0
    count = 0
    for index in range(1, len(text)):
        if text[index] != text[index - 1]:
            count = count + min(previous, current)
            previous = current
            current = 1
        else:
            current = current + 1
    count = count + min(previous, current)
    return count
