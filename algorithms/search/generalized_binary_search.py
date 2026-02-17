"""
Generalized Binary Search

Find the smallest value in a numeric range for which a monotonic boolean
predicate evaluates to True.  Instead of searching for a specific value in
an array, this version accepts an arbitrary predicate, allowing the same
binary search logic to be reused across many problem domains.

Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

Complexity:
    Time:  O(log n)
    Space: O(1)
"""

from __future__ import annotations

from collections.abc import Callable


def binary_search_first_true(
    low: int,
    high: int,
    predicate: Callable[[int], bool],
) -> int:
    """Find the smallest *x* in [low, high] where *predicate(x)* is True.

    The predicate must be monotonic: once it returns True for some value,
    it must return True for all larger values in the range.

    Args:
        low: Lower bound of the search range (inclusive).
        high: Upper bound of the search range (inclusive).
        predicate: A monotonic boolean function.

    Returns:
        The smallest *x* for which *predicate(x)* is True, or -1 if no
        such value exists in the range.

    Examples:
        >>> binary_search_first_true(0, 10, lambda x: x >= 7)
        7
        >>> binary_search_first_true(0, 10, lambda x: x * x >= 25)
        5
        >>> binary_search_first_true(0, 5, lambda x: x > 10)
        -1
    """
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if predicate(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == "__main__":
    print(binary_search_first_true(0, 10, lambda x: x >= 7))       # 7
    print(binary_search_first_true(0, 10, lambda x: x * x >= 25))  # 5
    print(binary_search_first_true(0, 5, lambda x: x > 10))        # -1
