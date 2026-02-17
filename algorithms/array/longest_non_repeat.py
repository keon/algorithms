"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters. Multiple algorithm variants are provided.

Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Complexity:
    Time:  O(n) for all variants
    Space: O(min(n, m)) where m is the charset size
"""

from __future__ import annotations


def longest_non_repeat_v1(string: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Args:
        string: Input string to search.

    Returns:
        Length of the longest non-repeating substring.

    Examples:
        >>> longest_non_repeat_v1("abcabcbb")
        3
    """
    if string is None:
        return 0
    char_index = {}
    max_length = 0
    start = 0
    for index in range(len(string)):
        if string[index] in char_index:
            start = max(char_index[string[index]], start)
        char_index[string[index]] = index + 1
        max_length = max(max_length, index - start + 1)
    return max_length


def longest_non_repeat_v2(string: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Args:
        string: Input string to search.

    Returns:
        Length of the longest non-repeating substring.

    Examples:
        >>> longest_non_repeat_v2("abcabcbb")
        3
    """
    if string is None:
        return 0
    start, max_length = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            max_length = max(max_length, index - start + 1)
        used_char[char] = index
    return max_length


def get_longest_non_repeat_v1(string: str) -> tuple[int, str]:
    """Find the longest substring without repeating characters.

    Args:
        string: Input string to search.

    Returns:
        A tuple of (length, substring) for the longest non-repeating substring.

    Examples:
        >>> get_longest_non_repeat_v1("abcabcbb")
        (3, 'abc')
    """
    if string is None:
        return 0, ""
    substring = ""
    char_index = {}
    max_length = 0
    start = 0
    for index in range(len(string)):
        if string[index] in char_index:
            start = max(char_index[string[index]], start)
        char_index[string[index]] = index + 1
        if index - start + 1 > max_length:
            max_length = index - start + 1
            substring = string[start : index + 1]
    return max_length, substring


def get_longest_non_repeat_v2(string: str) -> tuple[int, str]:
    """Find the longest substring without repeating characters.

    Args:
        string: Input string to search.

    Returns:
        A tuple of (length, substring) for the longest non-repeating substring.

    Examples:
        >>> get_longest_non_repeat_v2("abcabcbb")
        (3, 'abc')
    """
    if string is None:
        return 0, ""
    substring = ""
    start, max_length = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            if index - start + 1 > max_length:
                max_length = index - start + 1
                substring = string[start : index + 1]
        used_char[char] = index
    return max_length, substring


def get_longest_non_repeat_v3(string: str) -> tuple[int, str]:
    """Find the longest substring without repeating characters using sliding window.

    Args:
        string: Input string to search.

    Returns:
        A tuple of (length, substring) for the longest non-repeating substring.

    Examples:
        >>> get_longest_non_repeat_v3("abcabcbb")
        (3, 'abc')
    """
    longest_substring = ""
    seen = set()
    start_index = 0
    for i in range(len(string)):
        while string[i] in seen:
            seen.remove(string[start_index])
            start_index += 1
        seen.add(string[i])
        longest_substring = max(longest_substring, string[start_index : i + 1], key=len)
    return len(longest_substring), longest_substring
