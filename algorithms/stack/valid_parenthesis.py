"""
Valid Parentheses

Determine if a string containing only '(', ')', '{', '}', '[' and ']'
has valid (properly closed and nested) brackets.

Reference: https://leetcode.com/problems/valid-parentheses/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def is_valid(s: str) -> bool:
    """Check if the bracket string is valid.

    Args:
        s: A string containing only bracket characters.

    Returns:
        True if the brackets are valid, False otherwise.

    Examples:
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
    """
    stack: list[str] = []
    matching = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching and (not stack or matching[char] != stack.pop()):
                return False
    return not stack
