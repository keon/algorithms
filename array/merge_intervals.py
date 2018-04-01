"""
Given a collection of intervals, merge all overlapping intervals.
"""
import unittest


class Interval:
    """
    In mathematics, a (real) interval is a set of real
    numbers with the property that any number that lies
    between two numbers in the set is also included in the set.
    """

    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval ({self.start}, {self.end})"

    def __iter__(self):
        return iter(range(self.start, self.end))

    def __getitem__(self, index):
        if index < 0:
            return self.end + index
        return self.start + index

    def __len__(self):
        return self.end - self.start

    def __contains__(self, item):
        if self.start >= item >= self.end:
            return True
        return False

    def __eq__(self, other):
        if self.start == other.start and self.end == other.end:
            return True
        return False

    def as_list(self):
        """ Return interval as list. """
        return list(self)

    @staticmethod
    def merge(intervals):
        """ Merges two intervals into one. """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

    @staticmethod
    def print_intervals(intervals):
        """
        Prints out the intervals.
        """
        res = []
        for i in intervals:
            res.append(repr(i))
        print("".join(res))


def merge_v2(intervals):
    """ Merges intervals in the form of list. """
    if intervals is None:
        return None
    intervals.sort(key=lambda i: i[0])
    out = [intervals.pop(0)]
    for i in intervals:
        if out[-1][-1] >= i[0]:
            out[-1][-1] = max(out[-1][-1], i[-1])
        else:
            out.append(i)
    return out


class TestMergeInterval(unittest.TestCase):

    def test_merge(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = [Interval(i[0], i[1]) for i in interval_list]
        merged_intervals = Interval.merge(intervals)
        self.assertEqual(
            merged_intervals,
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
        )

    def test_merge_v2(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        merged_intervals = merge_v2(interval_list)
        self.assertEqual(
            merged_intervals,
            [[1, 6], [8, 10], [15, 18]]
        )


if __name__ == "__main__":
    unittest.main()
