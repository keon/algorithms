"""
In mathematics, a (real) interval is a set of real
 numbers with the property that any number that lies
 between two numbers in the set is also included in the set.
"""


class Interval:
    """
    A set of real numbers with methods to determine if other
     numbers are included in the set.
    Includes related methods to merge and print interval sets.
    """
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return "Interval ({}, {})".format(self.start, self.end)

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
        """ Merge two intervals into one. """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

    @staticmethod
    def print_intervals(intervals):
        """ Print out the intervals. """
        res = []
        for i in intervals:
            res.append(repr(i))
        print("".join(res))


def merge_intervals(intervals):
    """ Merge intervals in the form of a list. """
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
