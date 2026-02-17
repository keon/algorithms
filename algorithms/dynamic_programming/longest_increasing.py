"""
Longest Increasing Subsequence

Find the length of the longest strictly increasing subsequence in an array.

Reference: https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Complexity:
    longest_increasing_subsequence:
        Time:  O(n^2)
        Space: O(n)
    longest_increasing_subsequence_optimized:
        Time:  O(n * log(x))  where x is the max element
        Space: O(x)
    longest_increasing_subsequence_optimized2:
        Time:  O(n * log(n))
        Space: O(n)
"""

from __future__ import annotations


def longest_increasing_subsequence(sequence: list[int]) -> int:
    """Find length of the longest increasing subsequence using O(n^2) DP.

    Args:
        sequence: List of integers.

    Returns:
        Length of the longest strictly increasing subsequence.

    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                counts[i] = max(counts[i], counts[j] + 1)
    return max(counts)


def longest_increasing_subsequence_optimized(sequence: list[int]) -> int:
    """Find length of LIS using a segment tree for O(n*log(x)) time.

    Args:
        sequence: List of integers.

    Returns:
        Length of the longest strictly increasing subsequence.

    Examples:
        >>> longest_increasing_subsequence_optimized([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    max_val = max(sequence)
    tree = [0] * (max_val << 2)

    def _update(pos: int, left: int, right: int, target: int, vertex: int) -> None:
        if left == right:
            tree[pos] = vertex
            return
        mid = (left + right) >> 1
        if target <= mid:
            _update(pos << 1, left, mid, target, vertex)
        else:
            _update((pos << 1) | 1, mid + 1, right, target, vertex)
        tree[pos] = max(tree[pos << 1], tree[(pos << 1) | 1])

    def _get_max(pos: int, left: int, right: int, start: int, end: int) -> int:
        if left > end or right < start:
            return 0
        if left >= start and right <= end:
            return tree[pos]
        mid = (left + right) >> 1
        return max(
            _get_max(pos << 1, left, mid, start, end),
            _get_max((pos << 1) | 1, mid + 1, right, start, end),
        )

    ans = 0
    for element in sequence:
        cur = _get_max(1, 0, max_val, 0, element - 1) + 1
        ans = max(ans, cur)
        _update(1, 0, max_val, element, cur)
    return ans


def longest_increasing_subsequence_optimized2(sequence: list[int]) -> int:
    """Find length of LIS using coordinate-compressed segment tree for O(n*log(n)).

    Args:
        sequence: List of integers.

    Returns:
        Length of the longest strictly increasing subsequence.

    Examples:
        >>> longest_increasing_subsequence_optimized2([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    length = len(sequence)
    tree = [0] * (length << 2)
    sorted_seq = sorted((x, -i) for i, x in enumerate(sequence))

    def _update(pos: int, left: int, right: int, target: int, vertex: int) -> None:
        if left == right:
            tree[pos] = vertex
            return
        mid = (left + right) >> 1
        if target <= mid:
            _update(pos << 1, left, mid, target, vertex)
        else:
            _update((pos << 1) | 1, mid + 1, right, target, vertex)
        tree[pos] = max(tree[pos << 1], tree[(pos << 1) | 1])

    def _get_max(pos: int, left: int, right: int, start: int, end: int) -> int:
        if left > end or right < start:
            return 0
        if left >= start and right <= end:
            return tree[pos]
        mid = (left + right) >> 1
        return max(
            _get_max(pos << 1, left, mid, start, end),
            _get_max((pos << 1) | 1, mid + 1, right, start, end),
        )

    ans = 0
    for tup in sorted_seq:
        i = -tup[1]
        cur = _get_max(1, 0, length - 1, 0, i - 1) + 1
        ans = max(ans, cur)
        _update(1, 0, length - 1, i, cur)
    return ans
