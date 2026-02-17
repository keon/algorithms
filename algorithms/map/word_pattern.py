"""
Word Pattern

Given a pattern and a string, determine if the string follows the same
pattern via a bijection between pattern letters and words.

Reference: https://leetcode.com/problems/word-pattern/description/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def word_pattern(pattern: str, string: str) -> bool:
    """Check if a string follows the given pattern.

    Args:
        pattern: A pattern string of lowercase letters.
        string: A space-separated string of words.

    Returns:
        True if the string follows the pattern, False otherwise.

    Examples:
        >>> word_pattern("abba", "dog cat cat dog")
        True
        >>> word_pattern("abba", "dog cat cat fish")
        False
    """
    mapping: dict[str, str] = {}
    mapped_values: set[str] = set()
    words = string.split()
    if len(words) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in mapping:
            if words[i] in mapped_values:
                return False
            mapping[pattern[i]] = words[i]
            mapped_values.add(words[i])
        else:
            if mapping[pattern[i]] != words[i]:
                return False
    return True
