"""
Longest Common Substring

Given two strings where the second contains all distinct characters,
find the longest common substring using index mapping.

Reference: https://en.wikipedia.org/wiki/Longest_common_substring_problem

Complexity:
    Time:  O(n log n) expected, O(n * m) worst case
    Space: O(n)
"""

from __future__ import annotations


def max_common_sub_string(s1: str, s2: str) -> str:
    """Find the longest common substring between s1 and s2.

    Assumes s2 has all unique characters, enabling an index-based
    matching approach.

    Args:
        s1: First input string.
        s2: Second input string with all distinct characters.

    Returns:
        The longest common substring.

    Examples:
        >>> max_common_sub_string("abcdef", "acdbef")
        'ef'
    """
    char_index = {s2[i]: i for i in range(len(s2))}
    max_length = 0
    best_substring = ""
    i = 0
    while i < len(s1):
        if s1[i] in char_index:
            j = char_index[s1[i]]
            k = i
            while j < len(s2) and k < len(s1) and s1[k] == s2[j]:
                k += 1
                j += 1
            if k - i > max_length:
                max_length = k - i
                best_substring = s1[i:k]
            i = k
        else:
            i += 1
    return best_substring
