"""
Limit Array Values

Filter an array to include only elements within a specified minimum and
maximum range (inclusive).

Reference: https://en.wikipedia.org/wiki/Clipping_(signal_processing)

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def limit(
    array: list[int],
    min_lim: int | None = None,
    max_lim: int | None = None,
) -> list[int]:
    """Return elements of array that fall within [min_lim, max_lim].

    Args:
        array: Source list of integers.
        min_lim: Minimum value (inclusive). Defaults to the array minimum.
        max_lim: Maximum value (inclusive). Defaults to the array maximum.

    Returns:
        A new list containing only values within the specified range.

    Examples:
        >>> limit([1, 2, 3, 4, 5], 2, 4)
        [2, 3, 4]
    """
    if len(array) == 0:
        return array

    if min_lim is None:
        min_lim = min(array)
    if max_lim is None:
        max_lim = max(array)

    return list(filter(lambda x: (min_lim <= x <= max_lim), array))
