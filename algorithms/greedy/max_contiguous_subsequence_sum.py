"""
Maximum Contiguous Subsequence Sum (Kadane's Algorithm)

Finds the maximum sum of a contiguous sub-array within a one-dimensional
array of numbers.  The algorithm is greedy / dynamic-programming hybrid.

Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def max_contiguous_subsequence_sum(arr: list[int]) -> int:
    """Return the maximum contiguous subsequence sum.

    The contiguous subsequence must contain at least one element.
    Returns 0 for an empty array.

    Args:
        arr: A list of integers.

    Returns:
        The maximum contiguous subsequence sum.

    Examples:
        >>> max_contiguous_subsequence_sum([-2, 3, 8, -1, 4])
        14
        >>> max_contiguous_subsequence_sum([-1, -3, -4])
        -1
        >>> max_contiguous_subsequence_sum([])
        0
    """
    if not arr:
        return 0

    max_sum = arr[0]
    current_sum = 0

    for value in arr:
        if current_sum + value < value:
            current_sum = value
        else:
            current_sum += value
        max_sum = max(max_sum, current_sum)

    return max_sum
