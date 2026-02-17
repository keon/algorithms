"""Gray code — generate n-bit Gray code sequences.

A Gray code is an ordering of binary numbers such that successive values
differ in exactly one bit. Used in error correction and rotary encoders.

Inspired by PR #932 (Simranstha045).
"""

from __future__ import annotations


def gray_code(n: int) -> list[int]:
    """Return the n-bit Gray code sequence as a list of integers.

    Uses the reflection (mirror) construction:
        gray(i) = i ^ (i >> 1)

    >>> gray_code(2)
    [0, 1, 3, 2]
    >>> gray_code(3)
    [0, 1, 3, 2, 6, 7, 5, 4]
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


def gray_to_binary(gray: int) -> int:
    """Convert a Gray-coded integer back to standard binary."""
    mask = gray >> 1
    while mask:
        gray ^= mask
        mask >>= 1
    return gray
