"""
Meeting Rooms

Given an array of meeting time intervals consisting of start and end times
[[s1, e1], [s2, e2], ...] (si < ei), determine if a person could attend
all meetings (i.e. no two meetings overlap).

Reference: https://leetcode.com/problems/meeting-rooms/

Complexity:
    Time:  O(n log n) best / O(n log n) average / O(n log n) worst
    Space: O(1)
"""

from __future__ import annotations


def can_attend_meetings(intervals: list) -> bool:
    """Determine whether all meetings can be attended without overlap.

    Args:
        intervals: List of interval objects with *start* and *end* attributes.

    Returns:
        True if a person can attend all meetings, False otherwise.

    Examples:
        >>> # With intervals [[0,30],[5,10],[15,20]] the answer is False.
        >>> # With intervals [[7,10],[2,4]] the answer is True.
    """
    intervals = sorted(intervals, key=lambda x: x.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True
