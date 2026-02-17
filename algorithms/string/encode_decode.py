"""
Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string, and
decode it back to the original list of strings.

Reference: https://leetcode.com/problems/encode-and-decode-strings/

Complexity:
    Time:  O(n) for both encode and decode
    Space: O(n)
"""

from __future__ import annotations


def encode(strs: str) -> str:
    """Encode a space-separated string into a length-prefixed format.

    Args:
        strs: A space-separated string of words.

    Returns:
        A single encoded string with length-prefixed words.

    Examples:
        >>> encode("keon is awesome")
        '4:keon2:is7:awesome'
    """
    result = ""
    for word in strs.split():
        result += str(len(word)) + ":" + word
    return result


def decode(text: str) -> list[str]:
    """Decode a length-prefixed string back into a list of strings.

    Args:
        text: The encoded string with length-prefixed words.

    Returns:
        A list of the original decoded strings.

    Examples:
        >>> decode("4:keon2:is7:awesome")
        ['keon', 'is', 'awesome']
    """
    words: list[str] = []
    index = 0
    while index < len(text):
        colon_index = text.find(":", index)
        size = int(text[index:colon_index])
        words.append(text[colon_index + 1 : colon_index + 1 + size])
        index = colon_index + 1 + size
    return words
