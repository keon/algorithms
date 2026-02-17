"""
Max Sliding Window (Deque-based)

Given an array and a window size k, find the maximum element in each
sliding window using a monotonic deque that stores indices of elements
in decreasing order of their values.

Reference: https://leetcode.com/problems/sliding-window-maximum/

Complexity:
    Time:  O(n)
    Space: O(k)
"""

from __future__ import annotations

import collections


def max_sliding_window(arr: list[int], k: int) -> list[int]:
    """Find the maximum in each sliding window of size k.

    Uses a deque to maintain indices of useful elements in decreasing
    order. The front of the deque always holds the index of the current
    window maximum.

    Args:
        arr: Input array of integers.
        k: Window size.

    Returns:
        List of maximum values for each window position.

    Examples:
        >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
    """
    index_deque: collections.deque[int] = collections.deque()
    result: list[int] = []
    for i, value in enumerate(arr):
        while index_deque and arr[index_deque[-1]] < value:
            index_deque.pop()
        index_deque.append(i)
        if index_deque[0] == i - k:
            index_deque.popleft()
        if i >= k - 1:
            result.append(arr[index_deque[0]])
    return result
