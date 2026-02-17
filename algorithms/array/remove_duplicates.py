"""
Remove Duplicates

Remove duplicate elements from an array while preserving the original order.
Handles both hashable and unhashable items.

Reference: https://en.wikipedia.org/wiki/Duplicate_code

Complexity:
    Time:  O(n) for hashable items / O(n^2) worst case for unhashable items
    Space: O(n)
"""

from __future__ import annotations

from collections.abc import Hashable
from typing import Any


def remove_duplicates(array: list[Any]) -> list[Any]:
    """Remove duplicate elements from an array, preserving order.

    Uses a set for O(1) lookups on hashable items and falls back to
    linear search for unhashable items.

    Args:
        array: Input list potentially containing duplicates.

    Returns:
        New list with duplicates removed, original order preserved.

    Examples:
        >>> remove_duplicates([1, 1, 2, 2, 3])
        [1, 2, 3]
    """
    seen = set()
    unique_array = []

    for item in array:
        if isinstance(item, Hashable):
            if item not in seen:
                seen.add(item)
                unique_array.append(item)
        else:
            if item not in unique_array:
                unique_array.append(item)

    return unique_array
