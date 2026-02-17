"""
Goldbach's Conjecture

Every even integer greater than 2 can be expressed as the sum of two primes.
This module provides a function to find such a pair of primes and a helper
to verify the conjecture over a range.

Reference: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture

Complexity:
    Time:  O(n * sqrt(n))  per call (sieve could be used for batch queries)
    Space: O(1) per call
"""

from __future__ import annotations


def _is_prime(n: int) -> bool:
    """Return ``True`` if *n* is a prime number.

    Examples:
        >>> _is_prime(7)
        True
        >>> _is_prime(10)
        False
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def goldbach(n: int) -> tuple[int, int]:
    """Return two primes whose sum equals *n*.

    Args:
        n: An even integer greater than 2.

    Returns:
        A tuple ``(p, q)`` with ``p <= q`` and ``p + q == n`` where both
        ``p`` and ``q`` are prime.

    Raises:
        ValueError: If *n* is not an even integer greater than 2.

    Examples:
        >>> goldbach(4)
        (2, 2)
        >>> goldbach(28)
        (5, 23)
        >>> p, q = goldbach(100)
        >>> p + q == 100 and _is_prime(p) and _is_prime(q)
        True
    """
    if n <= 2 or n % 2 != 0:
        msg = f"n must be an even integer greater than 2, got {n}"
        raise ValueError(msg)

    for i in range(2, n // 2 + 1):
        if _is_prime(i) and _is_prime(n - i):
            return (i, n - i)

    # Should never be reached if Goldbach's conjecture holds
    msg = f"no prime pair found for {n}"  # pragma: no cover
    raise RuntimeError(msg)  # pragma: no cover


def verify_goldbach(limit: int) -> bool:
    """Verify Goldbach's conjecture for all even numbers from 4 to *limit*.

    Args:
        limit: Upper bound (inclusive) for verification.

    Returns:
        ``True`` if every even number in range can be expressed as a sum
        of two primes.

    Examples:
        >>> verify_goldbach(100)
        True
        >>> verify_goldbach(1000)
        True
    """
    return all(goldbach(n) is not None for n in range(4, limit + 1, 2))
