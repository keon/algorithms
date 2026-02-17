"""
Modular Exponentiation

Compute (base ^ exponent) % mod efficiently using binary exponentiation
(repeated squaring).

Reference: https://en.wikipedia.org/wiki/Modular_exponentiation

Complexity:
    Time:  O(log exponent)
    Space: O(1)
"""

from __future__ import annotations


def modular_exponential(base: int, exponent: int, mod: int) -> int:
    """Compute (base ^ exponent) % mod using binary exponentiation.

    Args:
        base: The base value.
        exponent: The exponent (must be non-negative).
        mod: The modulus.

    Returns:
        The result of (base ^ exponent) % mod.

    Raises:
        ValueError: If exponent is negative.

    Examples:
        >>> modular_exponential(5, 117, 19)
        1
    """
    if exponent < 0:
        raise ValueError("Exponent must be positive.")
    base %= mod
    result = 1

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod

    return result
