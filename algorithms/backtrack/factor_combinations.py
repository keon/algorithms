"""
Factor Combinations

Given an integer n, return all possible combinations of its factors.
Factors should be greater than 1 and less than n.

Reference: https://leetcode.com/problems/factor-combinations/

Complexity:
    Time:  O(n * log(n)) approximate
    Space: O(log(n)) recursion depth
"""

from __future__ import annotations


def get_factors(number: int) -> list[list[int]]:
    """Return all factor combinations of number using iteration.

    Args:
        number: A positive integer.

    Returns:
        A list of lists, each containing a valid factorization.

    Examples:
        >>> get_factors(12)
        [[2, 6], [2, 2, 3], [3, 4]]
    """
    todo: list[tuple[int, int, list[int]]] = [(number, 2, [])]
    combinations: list[list[int]] = []
    while todo:
        remaining, divisor, partial = todo.pop()
        while divisor * divisor <= remaining:
            if remaining % divisor == 0:
                combinations.append(partial + [divisor, remaining // divisor])
                todo.append((remaining // divisor, divisor, partial + [divisor]))
            divisor += 1
    return combinations


def recursive_get_factors(number: int) -> list[list[int]]:
    """Return all factor combinations of number using recursion.

    Args:
        number: A positive integer.

    Returns:
        A list of lists, each containing a valid factorization.

    Examples:
        >>> recursive_get_factors(12)
        [[2, 6], [2, 2, 3], [3, 4]]
    """

    def _factor(
        remaining: int,
        divisor: int,
        partial: list[int],
        combinations: list[list[int]],
    ) -> list[list[int]]:
        while divisor * divisor <= remaining:
            if remaining % divisor == 0:
                combinations.append(partial + [divisor, remaining // divisor])
                _factor(remaining // divisor, divisor, partial + [divisor],
                        combinations)
            divisor += 1
        return combinations

    return _factor(number, 2, [], [])
