"""
Contain String (strStr)

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Reference: https://leetcode.com/problems/implement-strstr/

Complexity:
    Time:  O(n * m) worst case, where n = len(haystack), m = len(needle)
    Space: O(1)
"""

from __future__ import annotations


def contain_string(haystack: str, needle: str) -> int:
    """Find the first occurrence of needle in haystack.

    Args:
        haystack: The string to search in.
        needle: The string to search for.

    Returns:
        The index of the first occurrence, or -1 if not found.

    Examples:
        >>> contain_string("hello", "ll")
        2
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for index in range(len(haystack)):
        if len(haystack) - index < len(needle):
            return -1
        if haystack[index:index + len(needle)] == needle:
            return index
    return -1
