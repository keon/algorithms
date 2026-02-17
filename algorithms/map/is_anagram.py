"""
Is Anagram

Determine whether two strings are anagrams of each other by comparing
character frequency maps.

Reference: https://leetcode.com/problems/valid-anagram/description/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def is_anagram(s: str, t: str) -> bool:
    """Check if string t is an anagram of string s.

    Args:
        s: First string.
        t: Second string.

    Returns:
        True if t is an anagram of s, False otherwise.

    Examples:
        >>> is_anagram("anagram", "nagaram")
        True
        >>> is_anagram("rat", "car")
        False
    """
    freq_s: dict[str, int] = {}
    freq_t: dict[str, int] = {}
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    return freq_s == freq_t
