"""Exponential search — locate an element in a sorted array.

First finds a range where the target may lie by doubling the index,
then performs binary search within that range. Useful when the target
is near the beginning of a large or unbounded list.

Time: O(log i) where i is the index of the target.

Inspired by PR #867 (yuviii99).
"""

from __future__ import annotations


def exponential_search(arr: list[int], target: int) -> int:
    """Return the index of *target* in sorted *arr*, or -1 if absent."""
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    bound = 1
    while bound < len(arr) and arr[bound] <= target:
        bound *= 2
    low = bound // 2
    high = min(bound, len(arr) - 1)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
