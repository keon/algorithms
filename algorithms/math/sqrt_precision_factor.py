"""
Square Root by Newton's Method

Compute the square root of a positive number using Newton's method
(Babylonian method) with a configurable precision factor.

Reference: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root

Complexity:
    Time:  O(log(1/epsilon)) iterations for convergence
    Space: O(1)
"""

from __future__ import annotations


def square_root(n: float, epsilon: float = 0.001) -> float:
    """Compute the square root of n with maximum absolute error epsilon.

    Args:
        n: A positive number.
        epsilon: Maximum allowed absolute error.

    Returns:
        An approximation of sqrt(n).

    Examples:
        >>> abs(square_root(5, 0.001) - 2.236) < 0.002
        True
    """
    guess = n / 2

    while abs(guess * guess - n) > epsilon:
        guess = (guess + (n / guess)) / 2

    return guess
