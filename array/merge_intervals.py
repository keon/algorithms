"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

>>> intervals_data = [[1,3],[2,6],[8,10],[15,18]]
>>> intervals = []
>>> for start, end in intervals_data:
...     intervals.append(Interval(start, end))
>>>
>>> assert repr(Interval.merge(intervals)) == \
    "[Interval [1, 6], Interval [8, 10], Interval [15, 18]]"
>>> # assert repr(Interval.merge_v2(intervals)) == \
    "[Interval [1, 6], Interval [8, 10], Interval [15, 18]]"
"""


class Interval:
    """
    In mathematics, a (real) interval is a set of real
    numbers with the property that any number that lies
    between two numbers in the set is also included in the set.
    https://en.wikipedia.org/wiki/Interval_(mathematics)
    """

    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval [{self.start}, {self.end}]"

    def __iter__(self):
        return range(self.start, self.end)

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

    # Intervals should support item assignment ?
    # @staticmethod
    # def merge_v2(intervals):
    #     if intervals is None:
    #         return None
    #     intervals.sort(key=lambda i: i.start)
    #     out = [intervals.pop(0)]
    #     for i in intervals:
    #         if out[-1][-1] >= i[0]:
    #             out[-1][-1] = max(out[-1][-1], i[-1])
    #         else:
    #             out.append(i)
    #     return out


if __name__ == "__main__":
    import doctest
    doctest.testmod()
