"""
Trimmed Mean

Compute the mean of an array after discarding a given percentage of the
highest and lowest values. Useful for robust averaging in scoring systems.

Reference: https://en.wikipedia.org/wiki/Truncated_mean

Complexity:
    Time:  O(n log n) due to sorting
    Space: O(n) for the trimmed copy
"""

from __future__ import annotations


def trimmean(array: list[float], percentage: float) -> float:
    """Calculate the trimmed mean of an array.

    Discards the top and bottom halves of the given percentage before
    computing the arithmetic mean.

    Args:
        array: List of numeric values.
        percentage: Total percentage to trim (split equally between
            top and bottom). E.g., 20 trims the top 10% and bottom 10%.

    Returns:
        The trimmed arithmetic mean.

    Examples:
        >>> trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20)
        5.5
    """
    ratio = percentage / 200
    array.sort()
    trim_count = int(len(array) * ratio)
    trimmed = array[trim_count:len(array) - trim_count]
    total = 0
    for value in trimmed:
        total += value
    return total / len(trimmed)
