"""
Rabin-Miller Primality Test

A probabilistic primality test where returning False guarantees the number
is composite, and returning True means the number is probably prime with
a 4^(-k) chance of error.

Reference: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

Complexity:
    Time:  O(k * log^2(n))
    Space: O(1)
"""

from __future__ import annotations

import random


def is_prime(n: int, k: int) -> bool:
    """Test if n is probably prime using the Rabin-Miller algorithm.

    Args:
        n: The integer to test for primality.
        k: The number of rounds of testing (higher = more accurate).

    Returns:
        True if n is probably prime, False if n is definitely composite.

    Examples:
        >>> is_prime(7, 2)
        True
        >>> is_prime(6, 2)
        False
    """

    def _pow2_factor(num: int) -> tuple[int, float]:
        """Factor num into 2^power * odd_part.

        Args:
            num: The integer to factor.

        Returns:
            A tuple (power, odd_part).
        """
        power = 0
        while num % 2 == 0:
            num /= 2
            power += 1
        return power, num

    def _valid_witness(a: int) -> bool:
        """Check if a is a witness for the compositeness of n.

        Args:
            a: The potential witness value.

        Returns:
            True if a proves n is composite, False otherwise.
        """
        x = pow(int(a), int(d), int(n))

        if x == 1 or x == n - 1:
            return False

        for _ in range(r - 1):
            x = pow(int(x), int(2), int(n))

            if x == 1:
                return True
            if x == n - 1:
                return False

        return True

    if n < 5:
        return n == 2 or n == 3

    r, d = _pow2_factor(n - 1)

    for _ in range(k):
        if _valid_witness(random.randrange(2, n - 2)):
            return False

    return True
