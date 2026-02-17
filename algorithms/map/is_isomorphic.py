"""
Isomorphic Strings

Determine if two strings are isomorphic. Two strings are isomorphic if
characters in s can be mapped to characters in t while preserving order,
with a one-to-one mapping.

Reference: https://leetcode.com/problems/isomorphic-strings/description/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def is_isomorphic(s: str, t: str) -> bool:
    """Check if two strings are isomorphic.

    Args:
        s: Source string.
        t: Target string.

    Returns:
        True if s and t are isomorphic, False otherwise.

    Examples:
        >>> is_isomorphic("egg", "add")
        True
        >>> is_isomorphic("foo", "bar")
        False
    """
    if len(s) != len(t):
        return False
    mapping: dict[str, str] = {}
    mapped_values: set[str] = set()
    for i in range(len(s)):
        if s[i] not in mapping:
            if t[i] in mapped_values:
                return False
            mapping[s[i]] = t[i]
            mapped_values.add(t[i])
        else:
            if mapping[s[i]] != t[i]:
                return False
    return True
