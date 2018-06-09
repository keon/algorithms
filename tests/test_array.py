from algorithms.arrays import (
    delete_nth, delete_nth_naive,
    flatten_iter, flatten,
    garage,
    josephus,
    longest_non_repeat_v1, longest_non_repeat_v2,
    Interval, merge_intervals,
    missing_ranges,
    move_zeros,
    plus_one_v1, plus_one_v2, plus_one_v3,
    rotate_v1, rotate_v2, rotate_v3,
    summarize_ranges,
    three_sum,
    two_sum,
    max_ones_index
)

import unittest


class TestJosephus(unittest.TestCase):

    def test_josephus(self):

        a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        josephus_generator = josephus(a, 3)
        self.assertEqual(next(josephus_generator), '3')
        self.assertEqual(next(josephus_generator), '6')
        self.assertEqual(next(josephus_generator), '9')
        self.assertEqual(next(josephus_generator), '4')
        self.assertEqual(next(josephus_generator), '8')
        self.assertEqual(next(josephus_generator), '5')
        self.assertEqual(next(josephus_generator), '2')
        self.assertEqual(next(josephus_generator), '7')
        self.assertEqual(next(josephus_generator), '1')
        self.assertRaises(StopIteration, next, josephus_generator)


class TestDeleteNth(unittest.TestCase):

    def test_delete_nth_naive(self):

        self.assertListEqual(delete_nth_naive(
                             [20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth_naive(
                             [1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth_naive(
                             [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth_naive([], n=5),
                             [])
        self.assertListEqual(delete_nth_naive(
                             [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])

    def test_delete_nth(self):

        self.assertListEqual(delete_nth([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])
        self.assertListEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])
        self.assertListEqual(delete_nth([], n=5),
                             [])
        self.assertListEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])


class TestFlatten(unittest.TestCase):

    def test_flatten(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [2, 1, 3, 4, 5, 6, 7, 8])

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [3, 4, 5, 6, 7, 8])

        nested_list = [[], [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [8])

    def test_flatten_iter(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 2)
        self.assertEqual(next(flattened), 1)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[], [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)


class TestGarage(unittest.TestCase):

    def test_garage(self):

        initial = [1, 2, 3, 0, 4]
        final = [0, 3, 2, 1, 4]
        steps, seq = garage(initial, final)

        self.assertEqual(steps, 4)
        self.assertListEqual(seq, [[0, 2, 3, 1, 4],
                                   [2, 0, 3, 1, 4],
                                   [2, 3, 0, 1, 4],
                                   [0, 3, 2, 1, 4]])


class TestLongestNonRepeat(unittest.TestCase):

    def test_longest_non_repeat_v1(self):

        string = "abcabcbb"
        self.assertEqual(longest_non_repeat_v1(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat_v1(string), 1)

        string = "pwwkew"
        self.assertEqual(longest_non_repeat_v1(string), 3)

    def test_longest_non_repeat_v2(self):

        string = "abcabcbb"
        self.assertEqual(longest_non_repeat_v2(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat_v2(string), 1)

        string = "pwwkew"
        self.assertEqual(longest_non_repeat_v2(string), 3)


class TestMaxOnesIndex(unittest.TestCase):

    def test_max_ones_index(self):

        self.assertEqual(9, max_ones_index([1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]))
        self.assertEqual(3, max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]))
        self.assertEqual(-1, max_ones_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


class TestMergeInterval(unittest.TestCase):

    def test_merge(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = [Interval(i[0], i[1]) for i in interval_list]
        merged_intervals = Interval.merge(intervals)
        self.assertEqual(
            merged_intervals,
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
        )

    def test_merge_intervals(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        merged_intervals = merge_intervals(interval_list)
        self.assertEqual(
            merged_intervals,
            [[1, 6], [8, 10], [15, 18]]
        )


class TestMissingRanges(unittest.TestCase):

    def test_missing_ranges(self):

        arr = [3, 5, 10, 11, 12, 15, 19]

        self.assertListEqual(missing_ranges(arr, 0, 20),
                             [(0, 2), (4, 4), (6, 9),
                              (13, 14), (16, 18), (20, 20)])

        self.assertListEqual(missing_ranges(arr, 6, 100),
                             [(6, 9), (13, 14), (16, 18), (20, 100)])


class TestMoveZeros(unittest.TestCase):

    def test_move_zeros(self):

        self.assertListEqual(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]),
                             [False, 1, 1, 2, 1, 3, "a", 0, 0])

        self.assertListEqual(move_zeros([0, 34, 'rahul', [], None, 0, True, 0]),
                             [34, 'rahul', [], None, True, 0, 0, 0])


class TestPlusOne(unittest.TestCase):

    def test_plus_one_v1(self):

        self.assertListEqual(plus_one_v1([0]), [1])
        self.assertListEqual(plus_one_v1([9]), [1, 0])
        self.assertListEqual(plus_one_v1([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v1([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v1([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])

    def test_plus_one_v2(self):

        self.assertListEqual(plus_one_v2([0]), [1])
        self.assertListEqual(plus_one_v2([9]), [1, 0])
        self.assertListEqual(plus_one_v2([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])

    def test_plus_one_v3(self):

        self.assertListEqual(plus_one_v3([0]), [1])
        self.assertListEqual(plus_one_v3([9]), [1, 0])
        self.assertListEqual(plus_one_v3([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 8, 0, 0, 9]),
                             [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 9, 9]),
                             [1, 0, 0, 0, 0])


class TestRotateArray(unittest.TestCase):

    def test_rotate_v1(self):

        self.assertListEqual(rotate_v1([1, 2, 3, 4, 5, 6, 7], k=3),
                                       [5, 6, 7, 1, 2, 3, 4])
        self.assertListEqual(rotate_v1([1, 2, 3, 4, 5, 6, 7], k=1),
                                       [7, 1, 2, 3, 4, 5, 6])
        self.assertListEqual(rotate_v1([1, 2, 3, 4, 5, 6, 7], k=7),
                                       [1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual(rotate_v1([1, 2], k=111), [2, 1])

    def test_rotate_v2(self):

        self.assertListEqual(rotate_v2([1, 2, 3, 4, 5, 6, 7], k=3),
                                       [5, 6, 7, 1, 2, 3, 4])
        self.assertListEqual(rotate_v2([1, 2, 3, 4, 5, 6, 7], k=1),
                                       [7, 1, 2, 3, 4, 5, 6])
        self.assertListEqual(rotate_v2([1, 2, 3, 4, 5, 6, 7], k=7),
                                       [1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual(rotate_v2([1, 2], k=111), [2, 1])

    def test_rotate_v3(self):

        self.assertListEqual(rotate_v3([1, 2, 3, 4, 5, 6, 7], k=3),
                                       [5, 6, 7, 1, 2, 3, 4])
        self.assertListEqual(rotate_v3([1, 2, 3, 4, 5, 6, 7], k=1),
                                       [7, 1, 2, 3, 4, 5, 6])
        self.assertListEqual(rotate_v3([1, 2, 3, 4, 5, 6, 7], k=7),
                                       [1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual(rotate_v3([1, 2], k=111), [2, 1])


class TestSummaryRanges(unittest.TestCase):

    def test_summarize_ranges(self):

        self.assertListEqual(summarize_ranges([0, 1, 2, 4, 5, 7]),
                             [(0, 2), (4, 5), (7, 7)])
        self.assertListEqual(summarize_ranges([-5, -4, -3, 1, 2, 4, 5, 6]),
                             [(-5, -3), (1, 2), (4, 6)])
        self.assertListEqual(summarize_ranges([-2, -1, 0, 1, 2]),
                             [(-2, 2)])


class TestThreeSum(unittest.TestCase):

    def test_three_sum(self):

        self.assertSetEqual(three_sum([-1, 0, 1, 2, -1, -4]),
                            {(-1, 0, 1), (-1, -1, 2)})

        self.assertSetEqual(three_sum([-1, 3, 1, 2, -1, -4, -2]),
                            {(-4, 1, 3), (-2, -1, 3), (-1, -1, 2)})


class TestSuite(unittest.TestCase):

    def test_two_sum(self):

        self.assertTupleEqual((0, 2), two_sum([2, 11, 7, 9], target=9))
        self.assertTupleEqual((0, 3), two_sum([-3, 5, 2, 3, 8, -9], target=0))

        self.assertIsNone(two_sum([-3, 5, 2, 3, 8, -9], target=6))


if __name__ == '__main__':

    unittest.main()
