"""
Sieve of Eratosthenes

Generate all prime numbers less than n using an optimized sieve that skips
even numbers.

Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Complexity:
    Time:  O(n log log n)
    Space: O(n)
"""

from __future__ import annotations


def get_primes(n: int) -> list[int]:
    """Return all primes less than n using the Sieve of Eratosthenes.

    Args:
        n: Upper bound (exclusive). Must be a positive integer.

    Returns:
        A sorted list of all primes less than n.

    Raises:
        ValueError: If n is not positive.

    Examples:
        >>> get_primes(7)
        [2, 3, 5, 7]
    """
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    sieve_size = (n // 2 - 1) if n % 2 == 0 else (n // 2)
    sieve = [True for _ in range(sieve_size)]
    primes: list[int] = []
    if n >= 2:
        primes.append(2)
    for i in range(sieve_size):
        if sieve[i]:
            value_at_i = i * 2 + 3
            primes.append(value_at_i)
            for j in range(i, sieve_size, value_at_i):
                sieve[j] = False
    return primes
