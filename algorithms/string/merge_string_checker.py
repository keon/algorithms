"""
Merge String Checker

Determine if a given string can be formed by interleaving two other strings,
preserving the character order from each part.

Reference: https://leetcode.com/problems/interleaving-string/

Complexity:
    Time:  O(2^n) worst case for recursive, similar for iterative
    Space: O(n) for recursion depth / stack
"""

from __future__ import annotations


def is_merge_recursive(text: str, part1: str, part2: str) -> bool:
    """Check if text is an interleaving of part1 and part2 recursively.

    Args:
        text: The merged string to verify.
        part1: The first source string.
        part2: The second source string.

    Returns:
        True if text is a valid interleaving of part1 and part2.

    Examples:
        >>> is_merge_recursive("codewars", "cdw", "oears")
        True
    """
    if not part1:
        return text == part2
    if not part2:
        return text == part1
    if not text:
        return part1 + part2 == ""
    if text[0] == part1[0] and is_merge_recursive(text[1:], part1[1:], part2):
        return True
    return (text[0] == part2[0]
            and is_merge_recursive(text[1:], part1, part2[1:]))


def is_merge_iterative(text: str, part1: str, part2: str) -> bool:
    """Check if text is an interleaving of part1 and part2 iteratively.

    Args:
        text: The merged string to verify.
        part1: The first source string.
        part2: The second source string.

    Returns:
        True if text is a valid interleaving of part1 and part2.

    Examples:
        >>> is_merge_iterative("codewars", "cdw", "oears")
        True
    """
    tuple_list = [(text, part1, part2)]
    while tuple_list:
        string, first_part, second_part = tuple_list.pop()
        if string:
            if first_part and string[0] == first_part[0]:
                tuple_list.append((string[1:], first_part[1:], second_part))
            if second_part and string[0] == second_part[0]:
                tuple_list.append((string[1:], first_part, second_part[1:]))
        else:
            if not first_part and not second_part:
                return True
    return False
