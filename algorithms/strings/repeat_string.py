"""
Repeated String Match

Given two strings A and B, find the minimum number of times A has to be
repeated such that B is a substring of the result. Return -1 if impossible.

Reference: https://leetcode.com/problems/repeated-string-match/

Complexity:
    Time:  O(n * m) where n = len(A), m = len(B)
    Space: O(n * (m/n + 2))
"""

from __future__ import annotations


def repeat_string(base: str, target: str) -> int:
    """Find minimum repetitions of base needed to contain target as a substring.

    Args:
        base: The string to repeat.
        target: The string that should appear as a substring.

    Returns:
        The minimum number of repetitions, or -1 if not possible.

    Examples:
        >>> repeat_string("abcd", "cdabcdab")
        3
    """
    repetition_count = 1
    repeated = base
    max_count = (len(target) / len(base)) + 1
    while target not in repeated:
        repeated = repeated + base
        if repetition_count > max_count:
            repetition_count = -1
            break
        repetition_count = repetition_count + 1

    return repetition_count
