"""
Weighted Job Scheduling

Given a set of jobs with start times, finish times, and profits, find
the maximum profit subset such that no two jobs overlap.

Reference: https://en.wikipedia.org/wiki/Job-shop_scheduling

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations


class Job:
    """Represents a job with start time, finish time, and profit."""

    def __init__(self, start: int, finish: int, profit: int) -> None:
        self.start = start
        self.finish = finish
        self.profit = profit


def _binary_search(job: list[Job], start_index: int) -> int:
    """Find the latest non-conflicting job before start_index.

    Args:
        job: List of jobs sorted by finish time.
        start_index: Index of the current job.

    Returns:
        Index of the latest compatible job, or -1 if none exists.
    """
    left = 0
    right = start_index - 1

    while left <= right:
        mid = (left + right) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                left = mid + 1
            else:
                return mid
        else:
            right = mid - 1
    return -1


def schedule(job: list[Job]) -> int:
    """Find the maximum profit from non-overlapping jobs.

    Args:
        job: List of Job objects.

    Returns:
        Maximum achievable profit.

    Examples:
        >>> schedule([Job(1, 3, 2), Job(2, 3, 4)])
        4
    """
    job = sorted(job, key=lambda j: j.finish)

    length = len(job)
    table = [0 for _ in range(length)]

    table[0] = job[0].profit

    for i in range(1, length):
        incl_prof = job[i].profit
        pos = _binary_search(job, i)
        if pos != -1:
            incl_prof += table[pos]

        table[i] = max(incl_prof, table[i - 1])

    return table[length - 1]
