"""
Histogram

Computes a histogram (frequency distribution) from a list of numerical values.
Each unique value is mapped to its count of occurrences.

Reference: https://en.wikipedia.org/wiki/Histogram

Complexity:
    Time:  O(n)
    Space: O(k) where k is the number of unique values
"""

from __future__ import annotations


def get_histogram(input_list: list[int]) -> dict[int, int]:
    """Build a histogram from a list of values.

    Args:
        input_list: A list of integers (may contain duplicates).

    Returns:
        A dict mapping each unique value to its frequency.

    Examples:
        >>> get_histogram([3, 3, 2, 1]) == {1: 1, 2: 1, 3: 2}
        True
        >>> get_histogram([2, 3, 5, 5, 5, 6, 4, 3, 7]) == {2: 1, 3: 2, 4: 1, 5: 3, 6: 1, 7: 1}
        True
    """
    histogram: dict[int, int] = {}
    for value in input_list:
        histogram[value] = histogram.get(value, 0) + 1
    return histogram
