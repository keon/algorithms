"""
Hailstone Sequence (Collatz Conjecture)

Generate the hailstone sequence starting from n: if n is even, next is n/2;
if n is odd, next is 3n + 1. The sequence ends when it reaches 1.

Reference: https://en.wikipedia.org/wiki/Collatz_conjecture

Complexity:
    Time:  O(unknown) - conjectured to always terminate
    Space: O(sequence length)
"""

from __future__ import annotations


def hailstone(n: int) -> list[int]:
    """Generate the hailstone sequence from n to 1.

    Args:
        n: The starting positive integer.

    Returns:
        The complete hailstone sequence from n down to 1.

    Examples:
        >>> hailstone(8)
        [8, 4, 2, 1]
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
    """
    sequence = [n]
    while n > 1:
        n = 3 * n + 1 if n % 2 != 0 else int(n / 2)
        sequence.append(n)
    return sequence
