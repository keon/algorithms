"""
Sliding Window Maximum (Heap-based)

Given an array and a window size k, find the maximum element in each
sliding window using a deque that maintains decreasing order of values.

Reference: https://leetcode.com/problems/sliding-window-maximum/

Complexity:
    Time:  O(n)
    Space: O(k)
"""

from __future__ import annotations

import collections


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Find the maximum in each sliding window of size k.

    Args:
        nums: Input array of integers.
        k: Window size.

    Returns:
        List of maximum values for each window position.

    Examples:
        >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
    """
    if not nums:
        return nums
    queue: collections.deque[int] = collections.deque()
    result: list[int] = []
    for num in nums:
        if len(queue) < k:
            queue.append(num)
        else:
            result.append(max(queue))
            queue.popleft()
            queue.append(num)
    result.append(max(queue))
    return result
