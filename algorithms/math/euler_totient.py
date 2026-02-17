"""
Euler's Totient Function

Compute Euler's totient function phi(n), which counts the number of integers
from 1 to n inclusive that are coprime to n.

Reference: https://en.wikipedia.org/wiki/Euler%27s_totient_function

Complexity:
    Time:  O(sqrt(n))
    Space: O(1)
"""

from __future__ import annotations


def euler_totient(n: int) -> int:
    """Compute Euler's totient function phi(n).

    Args:
        n: A positive integer.

    Returns:
        The count of integers in [1, n] coprime to n.

    Examples:
        >>> euler_totient(8)
        4
        >>> euler_totient(21)
        12
    """
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result
