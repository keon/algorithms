"""
Subsets via Bit Manipulation

Generate all possible subsets of a set of distinct integers using bitmask
enumeration. Each integer from 0 to 2^n - 1 represents a unique subset.

Reference: https://en.wikipedia.org/wiki/Power_set

Complexity:
    Time:  O(n * 2^n)
    Space: O(n * 2^n)
"""

from __future__ import annotations


def subsets(nums: list[int]) -> set[tuple[int, ...]]:
    """Return all subsets of the given list as a set of tuples.

    Uses bitmask enumeration: for each number from 0 to 2^n - 1, the
    set bits indicate which elements are included in that subset.

    Args:
        nums: A list of distinct integers.

    Returns:
        A set of tuples, each representing one subset.

    Examples:
        >>> sorted(subsets([1, 2, 3]))
        [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    length = len(nums)
    total = 1 << length
    result: set[tuple[int, ...]] = set()

    for mask in range(total):
        subset = tuple(
            number for bit_index, number in enumerate(nums) if mask & 1 << bit_index
        )
        result.add(subset)

    return result
