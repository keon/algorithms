"""
One Edit Distance

Given two strings, determine if they are exactly one edit distance apart.
An edit is an insertion, deletion, or replacement of a single character.

Reference: https://leetcode.com/problems/one-edit-distance/

Complexity:
    Time:  O(n) where n is the length of the shorter string
    Space: O(n) for string slicing
"""

from __future__ import annotations


def is_one_edit(source: str, target: str) -> bool:
    """Check if two strings are exactly one edit apart using slicing.

    Args:
        source: The first string.
        target: The second string.

    Returns:
        True if the strings are exactly one edit apart, False otherwise.

    Examples:
        >>> is_one_edit("abc", "abd")
        True
    """
    if len(source) > len(target):
        return is_one_edit(target, source)
    if len(target) - len(source) > 1 or target == source:
        return False
    for index in range(len(source)):
        if source[index] != target[index]:
            return (
                source[index + 1 :] == target[index + 1 :]
                or source[index:] == target[index + 1 :]
            )
    return True


def is_one_edit2(source: str, target: str) -> bool:
    """Check if two strings are exactly one edit apart using modification.

    Args:
        source: The first string.
        target: The second string.

    Returns:
        True if the strings are exactly one edit apart, False otherwise.

    Examples:
        >>> is_one_edit2("abc", "abd")
        True
    """
    source_length, target_length = len(source), len(target)
    if source_length > target_length:
        return is_one_edit2(target, source)
    if len(target) - len(source) > 1 or target == source:
        return False
    for index in range(len(source)):
        if source[index] != target[index]:
            if source_length == target_length:
                source = source[:index] + target[index] + source[index + 1 :]
            else:
                source = source[:index] + target[index] + source[index:]
            break
    return source == target or source == target[:-1]
