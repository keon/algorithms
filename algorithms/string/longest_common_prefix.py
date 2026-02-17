"""
Longest Common Prefix

Find the longest common prefix string amongst an array of strings.
Three approaches: horizontal scanning, vertical scanning, and divide and conquer.

Reference: https://leetcode.com/problems/longest-common-prefix/

Complexity:
    Time:  O(S) where S is the sum of all characters in all strings
    Space: O(1) for iterative, O(m * log n) for divide and conquer
"""

from __future__ import annotations


def _common_prefix(first: str, second: str) -> str:
    """Return the common prefix of two strings.

    Args:
        first: The first string.
        second: The second string.

    Returns:
        The common prefix shared by both strings.
    """
    if not first or not second:
        return ""
    index = 0
    while first[index] == second[index]:
        index = index + 1
        if index >= len(first) or index >= len(second):
            return first[0:index]
    return first[0:index]


def longest_common_prefix_v1(strings: list[str]) -> str:
    """Find longest common prefix using horizontal scanning.

    Args:
        strings: A list of strings to compare.

    Returns:
        The longest common prefix, or empty string if none exists.

    Examples:
        >>> longest_common_prefix_v1(["flower", "flow", "flight"])
        'fl'
    """
    if not strings:
        return ""
    result = strings[0]
    for index in range(len(strings)):
        result = _common_prefix(result, strings[index])
    return result


def longest_common_prefix_v2(strings: list[str]) -> str:
    """Find longest common prefix using vertical scanning.

    Args:
        strings: A list of strings to compare.

    Returns:
        The longest common prefix, or empty string if none exists.

    Examples:
        >>> longest_common_prefix_v2(["flower", "flow", "flight"])
        'fl'
    """
    if not strings:
        return ""
    for index in range(len(strings[0])):
        for string in strings[1:]:
            if index == len(string) or string[index] != strings[0][index]:
                return strings[0][0:index]
    return strings[0]


def longest_common_prefix_v3(strings: list[str]) -> str:
    """Find longest common prefix using divide and conquer.

    Args:
        strings: A list of strings to compare.

    Returns:
        The longest common prefix, or empty string if none exists.

    Examples:
        >>> longest_common_prefix_v3(["flower", "flow", "flight"])
        'fl'
    """
    if not strings:
        return ""
    return _longest_common_recursive(strings, 0, len(strings) - 1)


def _longest_common_recursive(strings: list[str], left: int, right: int) -> str:
    """Recursively find the longest common prefix using divide and conquer.

    Args:
        strings: The list of strings.
        left: The left index of the current partition.
        right: The right index of the current partition.

    Returns:
        The longest common prefix for the partition.
    """
    if left == right:
        return strings[left]
    mid = (left + right) // 2
    lcp_left = _longest_common_recursive(strings, left, mid)
    lcp_right = _longest_common_recursive(strings, mid + 1, right)
    return _common_prefix(lcp_left, lcp_right)
