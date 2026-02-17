"""
Is Rotated String

Given two strings, determine if the second is a rotated version of the first.
Two approaches are provided: concatenation check and brute force.

Reference: https://leetcode.com/problems/rotate-string/

Complexity:
    Time:  O(n) for concatenation approach, O(n^2) for brute force
    Space: O(n)
"""

from __future__ import annotations


def is_rotated(first: str, second: str) -> bool:
    """Check if second is a rotation of first using string concatenation.

    Args:
        first: The original string.
        second: The string to check as a rotation.

    Returns:
        True if second is a rotation of first, False otherwise.

    Examples:
        >>> is_rotated("hello", "llohe")
        True
    """
    if len(first) == len(second):
        return second in first + first
    else:
        return False


def is_rotated_v1(first: str, second: str) -> bool:
    """Check if second is a rotation of first using brute force comparison.

    Args:
        first: The original string.
        second: The string to check as a rotation.

    Returns:
        True if second is a rotation of first, False otherwise.

    Examples:
        >>> is_rotated_v1("hello", "llohe")
        True
    """
    if len(first) != len(second):
        return False
    if len(first) == 0:
        return True

    for offset in range(len(first)):
        if all(
            first[(offset + index) % len(first)] == second[index]
            for index in range(len(first))
        ):
            return True
    return False
