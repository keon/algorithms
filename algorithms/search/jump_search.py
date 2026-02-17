"""
Jump Search

Search for a target value in a sorted array by jumping ahead in fixed-size
blocks and then performing a linear search within the identified block.

Reference: https://en.wikipedia.org/wiki/Jump_search

Complexity:
    Time:  O(1) best / O(sqrt n) average / O(sqrt n) worst
    Space: O(1)
"""

from __future__ import annotations

import math


def jump_search(array: list[int], target: int) -> int:
    """Search for *target* in a sorted *array* using jump search.

    Args:
        array: Sorted list of integers in ascending order.
        target: Value to search for.

    Returns:
        Index of *target* in *array*, or -1 if not found.

    Examples:
        >>> jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        4
        >>> jump_search([1, 2, 3, 4, 5], 0)
        -1
    """
    length = len(array)
    block_size = int(math.sqrt(length))
    block_prev = 0
    block = block_size

    if array[length - 1] < target:
        return -1
    while block <= length and array[block - 1] < target:
        block_prev = block
        block += block_size

    while array[block_prev] < target:
        block_prev += 1
        if block_prev == min(block, length):
            return -1

    if array[block_prev] == target:
        return block_prev
    return -1
