"""
Decode String

Given an encoded string, return its decoded string. The encoding rule is
k[encoded_string], where the encoded_string inside the brackets is repeated
exactly k times.

Reference: https://leetcode.com/problems/decode-string/

Complexity:
    Time:  O(n * max_k) where n is the length of the string
    Space: O(n) for the stack
"""

from __future__ import annotations


def decode_string(text: str) -> str:
    """Decode an encoded string with nested repeat patterns.

    Args:
        text: The encoded string in the format k[encoded_string].

    Returns:
        The fully decoded string.

    Examples:
        >>> decode_string("3[a]2[bc]")
        'aaabcbc'
    """
    stack: list[tuple[str, int]] = []
    current_num = 0
    current_string = ""
    for char in text:
        if char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            prev_string, num = stack.pop()
            current_string = prev_string + num * current_string
        elif char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            current_string += char
    return current_string
