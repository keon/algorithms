"""
Fibonacci Number

Compute the n-th Fibonacci number using three different approaches:
recursive, list-based DP, and iterative.

Reference: https://en.wikipedia.org/wiki/Fibonacci_number

Complexity:
    fib_recursive:
        Time:  O(2^n)
        Space: O(n)  (call stack)
    fib_list:
        Time:  O(n)
        Space: O(n)
    fib_iter:
        Time:  O(n)
        Space: O(1)
"""

from __future__ import annotations


def fib_recursive(n: int) -> int:
    """Compute the n-th Fibonacci number recursively.

    Args:
        n: Non-negative integer index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Examples:
        >>> fib_recursive(10)
        55
    """
    assert n >= 0, 'n must be a positive integer'

    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_list(n: int) -> int:
    """Compute the n-th Fibonacci number using a list-based DP table.

    Args:
        n: Non-negative integer index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Examples:
        >>> fib_list(10)
        55
    """
    assert n >= 0, 'n must be a positive integer'

    list_results = [0, 1]
    for i in range(2, n + 1):
        list_results.append(list_results[i - 1] + list_results[i - 2])
    return list_results[n]


def fib_iter(n: int) -> int:
    """Compute the n-th Fibonacci number iteratively with constant space.

    Args:
        n: Non-negative integer index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Examples:
        >>> fib_iter(10)
        55
    """
    assert n >= 0, 'n must be positive integer'

    fib_1 = 0
    fib_2 = 1
    res = 0
    if n <= 1:
        return n
    for _ in range(n - 1):
        res = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = res
    return res
