"""
Misra-Gries Frequency Estimation

Given a list of items and a value k, returns every item that appears at least
n/k times, where n is the length of the list. Defaults to k=2 (majority
problem).

Reference: https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary

Complexity:
    Time:  O(n * k)
    Space: O(k)
"""

from __future__ import annotations


def misras_gries(array: list[int], k: int = 2) -> dict[str, int] | None:
    """Find all elements appearing at least n/k times.

    Args:
        array: A list of integers.
        k: The frequency threshold divisor (default 2).

    Returns:
        A dict mapping element (as string) to its frequency, or None
        if no element meets the threshold.

    Examples:
        >>> misras_gries([1, 4, 4, 4, 5, 4, 4])
        {'4': 5}
        >>> misras_gries([0, 0, 0, 1, 1, 1, 1])
        {'1': 4}
        >>> misras_gries([0, 0, 0, 0, 1, 1, 1, 2, 2], 3)
        {'0': 4, '1': 3}
    """
    keys: dict[str, int] = {}
    for item in array:
        val = str(item)
        if val in keys:
            keys[val] += 1
        elif len(keys) < k - 1:
            keys[val] = 1
        else:
            for key in list(keys):
                keys[key] -= 1
                if keys[key] == 0:
                    del keys[key]

    suspects = keys.keys()
    frequencies: dict[str, int] = {}
    for suspect in suspects:
        freq = _count_frequency(array, int(suspect))
        if freq >= len(array) / k:
            frequencies[suspect] = freq

    return frequencies if frequencies else None


def _count_frequency(array: list[int], element: int) -> int:
    """Count occurrences of element in array.

    Args:
        array: The list to search.
        element: The value to count.

    Returns:
        The number of occurrences.
    """
    return array.count(element)
