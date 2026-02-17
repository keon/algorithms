"""
Pattern Matching

Given a pattern and a string, determine if the string follows the same
pattern. A full match means a bijection between each letter in the pattern
and a non-empty substring in the string.

Reference: https://leetcode.com/problems/word-pattern-ii/

Complexity:
    Time:  O(n^m) where n is string length, m is pattern length
    Space: O(m) recursion depth plus mapping storage
"""

from __future__ import annotations


def pattern_match(pattern: str, string: str) -> bool:
    """Check whether a string matches a given pattern via bijection.

    Args:
        pattern: A pattern string of lowercase letters.
        string: The string to match against (lowercase letters).

    Returns:
        True if the string follows the pattern, False otherwise.

    Examples:
        >>> pattern_match("abab", "redblueredblue")
        True
        >>> pattern_match("aabb", "xyzabcxzyabc")
        False
    """
    return _backtrack(pattern, string, {})


def _backtrack(
    pattern: str,
    string: str,
    mapping: dict[str, str],
) -> bool:
    """Recursively attempt to match pattern to string using a mapping."""
    if len(pattern) == 0 and len(string) > 0:
        return False

    if len(pattern) == 0 and len(string) == 0:
        return True

    for end in range(1, len(string) - len(pattern) + 2):
        if pattern[0] not in mapping and string[:end] not in mapping.values():
            mapping[pattern[0]] = string[:end]
            if _backtrack(pattern[1:], string[end:], mapping):
                return True
            del mapping[pattern[0]]
        elif pattern[0] in mapping and mapping[pattern[0]] == string[:end]:
            if _backtrack(pattern[1:], string[end:], mapping):
                return True
    return False
