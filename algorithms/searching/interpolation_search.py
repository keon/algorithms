"""
Interpolation Search

Search for a target value in a uniformly distributed sorted array by
estimating the position of the target using linear interpolation.

Reference: https://en.wikipedia.org/wiki/Interpolation_search

Complexity:
    Time:  O(1) best / O(log log n) average / O(n) worst
    Space: O(1)
"""

from __future__ import annotations


def interpolation_search(array: list[int], search_key: int) -> int:
    """Search for *search_key* in a sorted *array* using interpolation search.

    Args:
        array: Sorted list of integers in ascending order.
        search_key: Value to search for.

    Returns:
        Index of *search_key* in *array*, or -1 if not found.

    Examples:
        >>> interpolation_search([-25, -12, -1, 10, 12, 15, 20, 41, 55], -1)
        2
        >>> interpolation_search([5, 10, 12, 14, 17, 20, 21], 55)
        -1
        >>> interpolation_search([5, 10, 12, 14, 17, 20, 21], -5)
        -1
    """
    high = len(array) - 1
    low = 0

    while (low <= high) and (array[low] <= search_key <= array[high]):
        pos = low + int(
            ((search_key - array[low]) * (high - low))
            / (array[high] - array[low])
        )

        if array[pos] == search_key:
            return pos

        if array[pos] < search_key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
