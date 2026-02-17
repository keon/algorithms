"""
Top 1 (Mode)

Find the most frequently occurring value(s) in an array. When multiple
values share the highest frequency, all are returned.

Reference: https://en.wikipedia.org/wiki/Mode_(statistics)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from typing import Any


def top_1(array: list[Any]) -> list[Any]:
    """Find the statistical mode(s) of an array.

    Args:
        array: Input list of comparable elements.

    Returns:
        List of element(s) with the highest frequency.

    Examples:
        >>> top_1([1, 1, 2, 2, 3])
        [1, 2]
    """
    frequency = {}
    for element in array:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    max_count = max(frequency.values())

    result = []
    for element, count in frequency.items():
        if count == max_count:
            result.append(element)

    return result
