"""
Recursive Binomial Coefficient

Calculate the binomial coefficient C(n, k) using a recursive formula with
the identity C(n, k) = (n/k) * C(n-1, k-1).

Reference: https://en.wikipedia.org/wiki/Binomial_coefficient

Complexity:
    Time:  O(k)
    Space: O(k) recursive stack
"""

from __future__ import annotations


def recursive_binomial_coefficient(n: int, k: int) -> int:
    """Calculate C(n, k) recursively, where n >= k.

    Args:
        n: Total number of items.
        k: Number of items to choose.

    Returns:
        The binomial coefficient C(n, k).

    Raises:
        ValueError: If k > n.

    Examples:
        >>> recursive_binomial_coefficient(5, 0)
        1
        >>> recursive_binomial_coefficient(8, 2)
        28
    """
    if k > n:
        raise ValueError("Invalid Inputs, ensure that n >= k")
    if k == 0 or n == k:
        return 1
    if k > n / 2:
        return recursive_binomial_coefficient(n, n - k)
    return int((n / k) * recursive_binomial_coefficient(n - 1, k - 1))
