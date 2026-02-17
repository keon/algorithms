"""
Regular Expression Matching

Implement regular expression matching with support for '.' (matches any
single character) and '*' (matches zero or more of the preceding element).

Reference: https://leetcode.com/problems/regular-expression-matching/

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
"""

from __future__ import annotations


def is_match(str_a: str, str_b: str) -> bool:
    """Determine whether str_a matches the pattern str_b.

    Args:
        str_a: Input string.
        str_b: Pattern string (may contain '.' and '*').

    Returns:
        True if str_a fully matches str_b, False otherwise.

    Examples:
        >>> is_match("aa", "a")
        False
        >>> is_match("aa", "a*")
        True
    """
    len_a, len_b = len(str_a) + 1, len(str_b) + 1
    matches = [[False] * len_b for _ in range(len_a)]

    matches[0][0] = True

    for i, element in enumerate(str_b[1:], 2):
        matches[0][i] = matches[0][i - 2] and element == "*"

    for i, char_a in enumerate(str_a, 1):
        for j, char_b in enumerate(str_b, 1):
            if char_b != "*":
                matches[i][j] = matches[i - 1][j - 1] and char_b in (char_a, ".")
            else:
                matches[i][j] |= matches[i][j - 2]

                if char_a == str_b[j - 2] or str_b[j - 2] == ".":
                    matches[i][j] |= matches[i - 1][j]

    return matches[-1][-1]
