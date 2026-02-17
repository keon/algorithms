"""
Factor Combinations

Given an integer n, return all possible combinations of its factors
(excluding 1 and n itself in the factorisation).

Reference: https://leetcode.com/problems/factor-combinations/

Complexity:
    Time:  O(n^(1/2) * log n)  (approximate, depends on factor density)
    Space: O(log n)
"""

from __future__ import annotations


def get_factors(n: int) -> list[list[int]]:
    """Return all factor combinations of *n* using recursion.

    Args:
        n: The number to factorise.

    Returns:
        List of factor lists.

    Examples:
        >>> get_factors(12)
        [[2, 6], [2, 2, 3], [3, 4]]
    """

    def _factor(
        n: int,
        i: int,
        combi: list[int],
        res: list[list[int]],
    ) -> list[list[int]]:
        while i * i <= n:
            if n % i == 0:
                res += (combi + [i, int(n / i)],)
                _factor(n / i, i, combi + [i], res)
            i += 1
        return res

    return _factor(n, 2, [], [])


def get_factors_iterative1(n: int) -> list[list[int]]:
    """Return all factor combinations using an explicit stack.

    Args:
        n: The number to factorise.

    Returns:
        List of factor lists.

    Examples:
        >>> get_factors_iterative1(12)
        [[2, 6], [3, 4], [2, 2, 3]]
    """
    todo: list[tuple[int, int, list[int]]] = [(n, 2, [])]
    res: list[list[int]] = []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                res += (combi + [i, n // i],)
                todo.append((n // i, i, combi + [i]))
            i += 1
    return res


def get_factors_iterative2(n: int) -> list[list[int]]:
    """Return all factor combinations using a stack-based approach.

    Args:
        n: The number to factorise.

    Returns:
        List of factor lists.

    Examples:
        >>> get_factors_iterative2(12)
        [[2, 2, 3], [2, 6], [3, 4]]
    """
    ans: list[list[int]] = []
    stack: list[int] = []
    x = 2
    while True:
        if x > n // x:
            if not stack:
                return ans
            ans.append(stack + [n])
            x = stack.pop()
            n *= x
            x += 1
        elif n % x == 0:
            stack.append(x)
            n //= x
        else:
            x += 1
