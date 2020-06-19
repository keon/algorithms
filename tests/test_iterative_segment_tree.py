from algorithms.tree.segment_tree.iterative_segment_tree import SegmentTree
from functools import reduce

import unittest


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class TestSegmentTree(unittest.TestCase):
    """
    Test for the Iterative Segment Tree data structure
    """

    def test_segment_tree_creation(self):
        arr = [2, 4, 3, 6, 8, 9, 3]
        max_segment_tree = SegmentTree(arr, max)
        min_segment_tree = SegmentTree(arr, min)
        sum_segment_tree = SegmentTree(arr, lambda a, b: a + b)
        gcd_segment_tree = SegmentTree(arr, gcd)
        self.assertEqual(max_segment_tree.tree, [None, 9, 8, 9, 4, 8, 9, 2, 4, 3, 6, 8, 9, 3])
        self.assertEqual(min_segment_tree.tree, [None, 2, 3, 2, 3, 6, 3, 2, 4, 3, 6, 8, 9, 3])
        self.assertEqual(sum_segment_tree.tree, [None, 35, 21, 14, 7, 14, 12, 2, 4, 3, 6, 8, 9, 3])
        self.assertEqual(gcd_segment_tree.tree, [None, 1, 1, 1, 1, 2, 3, 2, 4, 3, 6, 8, 9, 3])

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

    def test_max_segment_tree_with_updates(self):
        arr = [-1, 1, 10, 2, 9, -3, 8, 4, 7, 5, 6, 0]
        updates = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12}
        self.__test_all_segments_with_updates(arr, max, updates)

    def test_min_segment_tree_with_updates(self):
        arr = [1, 10, -2, 9, -3, 8, 4, -7, 5, 6, 11, -12]
        updates = {0: 7, 1: 2, 2: 6, 3: -14, 4: 5, 5: 4, 6: 7, 7: -10, 8: 9, 9: 10, 10: 12, 11: 1}
        self.__test_all_segments_with_updates(arr, min, updates)

    def test_sum_segment_tree_with_updates(self):
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, -11, -12]
        updates = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2, 11: 1}
        self.__test_all_segments_with_updates(arr, lambda a, b: a + b, updates)

    def test_gcd_segment_tree_with_updates(self):
        arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 14]
        updates = {0: 4, 1: 2, 2: 3, 3: 9, 4: 21, 5: 7, 6: 4, 7: 4, 8: 2, 9: 5, 10: 17, 11: 12, 12: 3}
        self.__test_all_segments_with_updates(arr, gcd, updates)

    def __test_all_segments(self, arr, fnc):
        """
        Test all possible segments in the tree
        :param arr: array to test
        :param fnc: function of the segment tree
        """
        segment_tree = SegmentTree(arr, fnc)
        self.__test_segments_helper(segment_tree, fnc, arr)

    def __test_all_segments_with_updates(self, arr, fnc, upd):
        """
        Test all possible segments in the tree with updates
        :param arr: array to test
        :param fnc: function of the segment tree
        :param upd: updates to test
        """
        segment_tree = SegmentTree(arr, fnc)
        for index, value in upd.items():
            arr[index] = value
            segment_tree.update(index, value)
            self.__test_segments_helper(segment_tree, fnc, arr)

    def __test_segments_helper(self, seg_tree, fnc, arr):
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                range_value = reduce(fnc, arr[i:j + 1])
                self.assertEqual(seg_tree.query(i, j), range_value)
