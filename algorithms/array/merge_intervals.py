"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals into a
consolidated set.

Reference: https://en.wikipedia.org/wiki/Interval_(mathematics)

Complexity:
    Time:  O(n log n) due to sorting
    Space: O(n)
"""

from __future__ import annotations


class Interval:
    """A numeric interval [start, end) with merge and comparison support.

    Args:
        start: Lower bound of the interval.
        end: Upper bound of the interval.
    """

    def __init__(self, start: int = 0, end: int = 0) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"Interval ({self.start}, {self.end})"

    def __iter__(self):
        return iter(range(self.start, self.end))

    def __getitem__(self, index: int) -> int:
        if index < 0:
            return self.end + index
        return self.start + index

    def __len__(self) -> int:
        return self.end - self.start

    def __contains__(self, item: int) -> bool:
        return self.start >= item >= self.end

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Interval):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def as_list(self) -> list[int]:
        """Return interval as a list of integers.

        Returns:
            List of integers in the interval range.
        """
        return list(self)

    @staticmethod
    def merge(intervals: list[Interval]) -> list[Interval]:
        """Merge overlapping intervals into a consolidated list.

        Args:
            intervals: List of Interval objects to merge.

        Returns:
            List of merged, non-overlapping Interval objects.

        Examples:
            >>> Interval.merge([Interval(1, 3), Interval(2, 6)])
            [Interval (1, 6)]
        """
        out = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if out and interval.start <= out[-1].end:
                out[-1].end = max(out[-1].end, interval.end)
            else:
                out += (interval,)
        return out

    @staticmethod
    def print_intervals(intervals: list[Interval]) -> str:
        """Format intervals as a string representation.

        Args:
            intervals: List of Interval objects to format.

        Returns:
            String representation of all intervals.

        Examples:
            >>> Interval.print_intervals([Interval(1, 3)])
            'Interval (1, 3)'
        """
        result = []
        for interval in intervals:
            result.append(repr(interval))
        return "".join(result)


def merge_intervals(intervals: list[list[int]]) -> list[list[int]] | None:
    """Merge overlapping intervals represented as nested lists.

    Args:
        intervals: List of [start, end] pairs to merge.

    Returns:
        List of merged [start, end] pairs, or None if input is None.

    Examples:
        >>> merge_intervals([[1, 3], [2, 6], [8, 10]])
        [[1, 6], [8, 10]]
    """
    if intervals is None:
        return None
    intervals.sort(key=lambda i: i[0])
    out = [intervals.pop(0)]
    for interval in intervals:
        if out[-1][-1] >= interval[0]:
            out[-1][-1] = max(out[-1][-1], interval[-1])
        else:
            out.append(interval)
    return out
