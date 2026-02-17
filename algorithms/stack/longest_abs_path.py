"""
Longest Absolute File Path

Given a string representing a file system in a special format, find the
length of the longest absolute path to a file. Directories and files
are separated by newlines; depth is indicated by tab characters.

Reference: https://leetcode.com/problems/longest-absolute-file-path/

Complexity:
    Time:  O(n)
    Space: O(d) where d is the maximum depth
"""

from __future__ import annotations


def length_longest_path(input_str: str) -> int:
    """Find the length of the longest absolute path to a file.

    Args:
        input_str: A string encoding the file system structure using
            newlines and tabs.

    Returns:
        Length of the longest absolute path to a file, or 0 if no file exists.

    Examples:
        >>> length_longest_path("dir\\n\\tfile.txt")
        12
    """
    current_length = 0
    max_length = 0
    stack: list[int] = []
    for segment in input_str.split("\n"):
        depth = segment.count("\t")
        while len(stack) > depth:
            current_length -= stack.pop()
        name_length = len(segment.strip("\t")) + 1
        stack.append(name_length)
        current_length += stack[-1]
        if "." in segment:
            max_length = max(max_length, current_length - 1)
    return max_length
