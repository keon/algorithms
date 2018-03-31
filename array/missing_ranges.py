"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""
import unittest


def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:
        res.append((start, hi))

    return res


class TestSuite(unittest.TestCase):

    def test_missing_ranges(self):

        arr = [3, 5, 10, 11, 12, 15, 19]

        self.assertListEqual(missing_ranges(arr, 0, 20),
                             [(0, 2), (4, 4), (6, 9), (13, 14), (16, 18), (20, 20)])

        self.assertListEqual(missing_ranges(arr, 6, 100),
                             [(6, 9), (13, 14), (16, 18), (20, 100)])


if __name__ == '__main__':

    unittest.main()
