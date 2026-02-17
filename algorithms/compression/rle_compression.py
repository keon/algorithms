"""
Run-Length Encoding (RLE)

A simple lossless compression algorithm that encodes consecutive repeated
characters as a count followed by the character. Decompression fully recovers
the original data.

Reference: https://en.wikipedia.org/wiki/Run-length_encoding

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def encode_rle(data: str) -> str:
    """Compress a string using run-length encoding.

    Args:
        data: The input string to compress.

    Returns:
        The RLE-encoded string.

    Examples:
        >>> encode_rle("aaabbc")
        '3a2b1c'
        >>> encode_rle("")
        ''
    """
    if not data:
        return ""

    encoded: str = ""
    prev_char: str = ""
    count: int = 1

    for char in data:
        if char != prev_char:
            if prev_char:
                encoded += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    return encoded + str(count) + prev_char


def decode_rle(data: str) -> str:
    """Decompress a run-length encoded string.

    Args:
        data: The RLE-encoded string.

    Returns:
        The decoded original string.

    Examples:
        >>> decode_rle("3a2b1c")
        'aaabbc'
        >>> decode_rle("")
        ''
    """
    decoded: str = ""
    count: str = ""

    for char in data:
        if not char.isdigit():
            decoded += char * int(count)
            count = ""
        else:
            count += char
    return decoded
