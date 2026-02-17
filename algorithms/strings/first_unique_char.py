"""
First Unique Character in a String

Given a string, find the first non-repeating character and return its index.
If no unique character exists, return -1.

Reference: https://leetcode.com/problems/first-unique-character-in-a-string/

Complexity:
    Time:  O(n^2) worst case due to nested comparisons
    Space: O(n) for the banned list
"""

from __future__ import annotations


def first_unique_char(text: str) -> int:
    """Find the index of the first non-repeating character in a string.

    Args:
        text: The input string to search.

    Returns:
        The index of the first unique character, or -1 if none exists.

    Examples:
        >>> first_unique_char("leetcode")
        0
    """
    if len(text) == 1:
        return 0
    banned: list[str] = []
    for index in range(len(text)):
        if all(text[index] != text[other] for other in range(index + 1, len(text))) and text[index] not in banned:
            return index
        else:
            banned.append(text[index])
    return -1
