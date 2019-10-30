from algorithms.tree.segment_tree.segment_tree import SegmentTree
from functools import reduce

import unittest


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class TestSegmentTree(unittest.TestCase):
    """
    Test for the Segment Tree data structure
    """
    def test_root_segment_tree(self):
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        max_segment_tree = SegmentTree(arr, max)
        min_segment_tree = SegmentTree(arr, min)
        sum_segment_tree = SegmentTree(arr, lambda a, b: a + b)
        gcd_segment_tree = SegmentTree(arr, gcd)
        self.assertEqual(max_segment_tree.segment[0], 10)
        self.assertEqual(min_segment_tree.segment[0], 1)
        self.assertEqual(sum_segment_tree.segment[0], 55)
        self.assertEqual(gcd_segment_tree.segment[0], 1)

    def test_max_segment_tree(self):
        arr = [-1, 1, 10, 2, 9, -3, 8, 4, 7, 5, 6, 0]
        self.__test_all_segments(arr, max)

    def test_min_segment_tree(self):
        arr = [1, 10, -2, 9, -3, 8, 4, -7, 5, 6, 11, -12]
        self.__test_all_segments(arr, min)

    def test_sum_segment_tree(self):
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, -11, -12]
        self.__test_all_segments(arr, lambda a, b: a + b)

    def test_gcd_segment_tree(self):
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 14]
        self.__test_all_segments(arr, gcd)

    def __test_all_segments(self, arr, fnc):
        """
        Test all possible segments in the tree
        :param arr: array to test
        :param fnc: function of the segment tree
        """
        segment_tree = SegmentTree(arr, fnc)
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                range_value = reduce(fnc, arr[i:j + 1])
                self.assertEqual(segment_tree.query(i, j), range_value)
