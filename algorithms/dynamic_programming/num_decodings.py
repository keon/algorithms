"""
Decode Ways

Given an encoded message of digits, count the total number of ways to
decode it where 'A' = 1, 'B' = 2, ..., 'Z' = 26.

Reference: https://leetcode.com/problems/decode-ways/

Complexity:
    Time:  O(n)
    Space: O(1) for num_decodings, O(n) for num_decodings2
"""

from __future__ import annotations


def num_decodings(enc_mes: str) -> int:
    """Count decoding ways using constant-space iteration.

    Args:
        enc_mes: String of digits representing the encoded message.

    Returns:
        Total number of ways to decode the message.

    Examples:
        >>> num_decodings("12")
        2
        >>> num_decodings("226")
        3
    """
    if not enc_mes or enc_mes[0] == "0":
        return 0
    last_char, last_two_chars = 1, 1
    for i in range(1, len(enc_mes)):
        last = last_char if enc_mes[i] != "0" else 0
        last_two = (
            last_two_chars
            if int(enc_mes[i - 1 : i + 1]) < 27 and enc_mes[i - 1] != "0"
            else 0
        )
        last_two_chars = last_char
        last_char = last + last_two
    return last_char


def num_decodings2(enc_mes: str) -> int:
    """Count decoding ways using a stack-based approach.

    Args:
        enc_mes: String of digits representing the encoded message.

    Returns:
        Total number of ways to decode the message.

    Examples:
        >>> num_decodings2("12")
        2
        >>> num_decodings2("226")
        3
    """
    if not enc_mes or enc_mes.startswith("0"):
        return 0
    stack = [1, 1]
    for i in range(1, len(enc_mes)):
        if enc_mes[i] == "0":
            if enc_mes[i - 1] == "0" or enc_mes[i - 1] > "2":
                return 0
            stack.append(stack[-2])
        elif 9 < int(enc_mes[i - 1 : i + 1]) < 27:
            stack.append(stack[-2] + stack[-1])
        else:
            stack.append(stack[-1])
    return stack[-1]
