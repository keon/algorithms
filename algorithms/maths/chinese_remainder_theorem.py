"""
Chinese Remainder Theorem

Solves a system of simultaneous congruences using the Chinese Remainder
Theorem. Given pairwise coprime moduli, finds the smallest positive integer
satisfying all congruences.

Reference: https://en.wikipedia.org/wiki/Chinese_remainder_theorem

Complexity:
    Time:  O(n * m) where n is the number of equations and m is the solution
    Space: O(1)
"""

from __future__ import annotations

from typing import List

from algorithms.maths.gcd import gcd


def solve_chinese_remainder(nums: List[int], rems: List[int]) -> int:
    """Find the smallest x satisfying x % nums[i] == rems[i] for all i.

    Args:
        nums: List of pairwise coprime moduli, each greater than 1.
        rems: List of remainders corresponding to each modulus.

    Returns:
        The smallest positive integer satisfying all congruences.

    Raises:
        Exception: If inputs are invalid or moduli are not pairwise coprime.

    Examples:
        >>> solve_chinese_remainder([3, 7, 10], [2, 3, 3])
        143
    """
    if not len(nums) == len(rems):
        raise Exception("nums and rems should have equal length")
    if not len(nums) > 0:
        raise Exception("Lists nums and rems need to contain at least one element")
    for num in nums:
        if not num > 1:
            raise Exception("All numbers in nums needs to be > 1")
    if not _check_coprime(nums):
        raise Exception("All pairs of numbers in nums are not coprime")
    k = len(nums)
    x = 1
    while True:
        i = 0
        while i < k:
            if x % nums[i] != rems[i]:
                break
            i += 1
        if i == k:
            return x
        x += 1


def _check_coprime(list_to_check: List[int]) -> bool:
    """Check whether all pairs of numbers in the list are coprime.

    Args:
        list_to_check: List of integers to check for pairwise coprimality.

    Returns:
        True if all pairs are coprime, False otherwise.
    """
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            if gcd(num, num2) != 1:
                return False
    return True
