"""Sentinel linear search — a small optimisation over naive linear search.

By placing the target at the end of the array (as a sentinel), we can
remove the bounds check from the inner loop, roughly halving comparisons.

Time: O(n) — same asymptotic complexity but fewer comparisons in practice.

Inspired by PR #907 (Abhishek-Pashte).
"""

from __future__ import annotations


def sentinel_search(arr: list[int], target: int) -> int:
    """Return the index of *target* in *arr*, or -1 if absent.

    Modifies (and restores) the last element temporarily.
    """
    n = len(arr)
    if n == 0:
        return -1
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last
    if i < n - 1 or arr[-1] == target:
        return i
    return -1
