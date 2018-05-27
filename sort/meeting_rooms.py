"""
Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""


def can_attend_meetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    intervals = sorted(intervals, key=lambda x: x.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True
