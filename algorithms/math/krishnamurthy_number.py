"""
Krishnamurthy Number

A Krishnamurthy number is a number whose sum of the factorials of its digits
equals the number itself (e.g., 145 = 1! + 4! + 5!).

Reference: https://en.wikipedia.org/wiki/Factorion

Complexity:
    Time:  O(d * m) where d is number of digits and m is max digit value
    Space: O(1)
"""

from __future__ import annotations


def _find_factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.
    """
    fact = 1
    while n != 0:
        fact *= n
        n -= 1
    return fact


def krishnamurthy_number(n: int) -> bool:
    """Check if n is a Krishnamurthy number (factorion).

    Args:
        n: The integer to check.

    Returns:
        True if n is a Krishnamurthy number, False otherwise.

    Examples:
        >>> krishnamurthy_number(145)
        True
        >>> krishnamurthy_number(357)
        False
    """
    if n == 0:
        return False
    sum_of_digits = 0
    temp = n

    while temp != 0:
        sum_of_digits += _find_factorial(temp % 10)
        temp //= 10

    return sum_of_digits == n
