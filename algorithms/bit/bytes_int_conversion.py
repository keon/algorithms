"""
Bytes-Integer Conversion

Convert between Python integers and raw byte sequences in both big-endian
and little-endian byte orders.

Reference: https://en.wikipedia.org/wiki/Endianness

Complexity:
    Time:  O(b) where b is the number of bytes in the representation
    Space: O(b)
"""

from __future__ import annotations

from collections import deque


def int_to_bytes_big_endian(number: int) -> bytes:
    """Convert a non-negative integer to bytes in big-endian order.

    Args:
        number: A non-negative integer to convert.

    Returns:
        A bytes object with the most significant byte first.

    Examples:
        >>> int_to_bytes_big_endian(17)
        b'\\x11'
    """
    byte_buffer: deque[int] = deque()
    while number > 0:
        byte_buffer.appendleft(number & 0xFF)
        number >>= 8
    return bytes(byte_buffer)


def int_to_bytes_little_endian(number: int) -> bytes:
    """Convert a non-negative integer to bytes in little-endian order.

    Args:
        number: A non-negative integer to convert.

    Returns:
        A bytes object with the least significant byte first.

    Examples:
        >>> int_to_bytes_little_endian(17)
        b'\\x11'
    """
    byte_buffer: list[int] = []
    while number > 0:
        byte_buffer.append(number & 0xFF)
        number >>= 8
    return bytes(byte_buffer)


def bytes_big_endian_to_int(byte_string: bytes) -> int:
    """Convert a big-endian byte sequence to an integer.

    Args:
        byte_string: Bytes with the most significant byte first.

    Returns:
        The decoded integer value.

    Examples:
        >>> bytes_big_endian_to_int(b'\\x11')
        17
    """
    number = 0
    for byte in byte_string:
        number <<= 8
        number += byte
    return number


def bytes_little_endian_to_int(byte_string: bytes) -> int:
    """Convert a little-endian byte sequence to an integer.

    Args:
        byte_string: Bytes with the least significant byte first.

    Returns:
        The decoded integer value.

    Examples:
        >>> bytes_little_endian_to_int(b'\\x11')
        17
    """
    number = 0
    exponent = 0
    for byte in byte_string:
        number += byte << exponent
        exponent += 8
    return number
