"""
Repeated Substring Pattern

Given a non-empty string, check if it can be constructed by taking a
substring of it and appending multiple copies of the substring together.

Reference: https://leetcode.com/problems/repeated-substring-pattern/

Complexity:
    Time:  O(n) for the string containment check
    Space: O(n)
"""

from __future__ import annotations


def repeat_substring(text: str) -> bool:
    """Check if a string is composed of a repeated substring pattern.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a repeated pattern, False otherwise.

    Examples:
        >>> repeat_substring("abab")
        True
    """
    doubled = (text + text)[1:-1]
    return text in doubled
