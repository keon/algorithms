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
    max_ones_index,
    trimmean,
    top_1,
    limit,
    n_sum
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

        string = "dvdf"
        self.assertEqual(longest_non_repeat_v1(string), 3)

        string = "asjrgapa"
        self.assertEqual(longest_non_repeat_v1(string), 6)

    def test_longest_non_repeat_v2(self):

        string = "abcabcbb"
        self.assertEqual(longest_non_repeat_v2(string), 3)

        string = "bbbbb"
        self.assertEqual(longest_non_repeat_v2(string), 1)

        string = "pwwkew"
        self.assertEqual(longest_non_repeat_v2(string), 3)

        string = "dvdf"
        self.assertEqual(longest_non_repeat_v2(string), 3)

        string = "asjrgapa"
        self.assertEqual(longest_non_repeat_v2(string), 6)


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


class TestTrimmean(unittest.TestCase):

    def test_trimmean(self):

        self.assertEqual(trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20), 5.5)
        self.assertEqual(trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 20), 6.0)


class TestTop1(unittest.TestCase):

    def test_top_1(self):
        self.assertListEqual(top_1([1 , 1, 2, 2, 3]), [1, 2])
        self.assertListEqual(top_1([1, 2, 3, 324, 234, 23, 23, 1, 23, 23]), [23])


class TestLimit(unittest.TestCase):

    def test_limit(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])
        self.assertListEqual(limit([1, 2, 3, 4, 5], 2), [2, 3, 4, 5])
        self.assertListEqual(limit([1, 2, 3, 4, 5], None, 4), [1, 2, 3, 4])


class TestNSum(unittest.TestCase):

    def test_n_sum(self):
        self.assertEqual(n_sum(2, [-3, 5, 2, 3, 8, -9], 6), [])  # noqa: E501
        self.assertEqual(n_sum(3, [-5, -4, -3, -2, -1, 0, 1, 2, 3], 0), sorted([[-5,2,3],[-2,0,2],[-4,1,3],[-3,1,2],[-1,0,1],[-2,-1,3],[-3,0,3]]))  # noqa: E501
        self.assertEqual(n_sum(3, [-1,0,1,2,-1,-4], 0), sorted([[-1,-1,2],[-1,0,1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [1, 0, -1, 0, -2, 2], 0), sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))  # noqa: E501
        self.assertEqual(n_sum(4, [7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 6, 4, -3, -2], 10), sorted([[-6, 2, 7, 7], [-6, 3, 6, 7], [-6, 4, 5, 7], [-6, 4, 6, 6], [-5, 1, 7, 7], [-5, 2, 6, 7], [-5, 3, 5, 7], [-5, 3, 6, 6], [-5, 4, 4, 7], [-5, 4, 5, 6], [-4, 0, 7, 7], [-4, 1, 6, 7], [-4, 2, 5, 7], [-4, 2, 6, 6], [-4, 3, 4, 7], [-4, 3, 5, 6], [-4, 4, 4, 6], [-3, -1, 7, 7], [-3, 0, 6, 7], [-3, 1, 5, 7], [-3, 1, 6, 6], [-3, 2, 4, 7], [-3, 2, 5, 6], [-3, 3, 4, 6], [-3, 4, 4, 5], [-2, -2, 7, 7], [-2, -1, 6, 7], [-2, 0, 5, 7], [-2, 0, 6, 6], [-2, 1, 4, 7], [-2, 1, 5, 6], [-2, 2, 3, 7], [-2, 2, 4, 6], [-2, 3, 4, 5], [-1, 0, 4, 7], [-1, 0, 5, 6], [-1, 1, 3, 7], [-1, 1, 4, 6], [-1, 2, 3, 6], [-1, 2, 4, 5], [-1, 3, 4, 4], [0, 1, 2, 7], [0, 1, 3, 6], [0, 1, 4, 5], [0, 2, 3, 5], [0, 2, 4, 4], [1, 2, 3, 4]]))  # noqa: E501

        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], 0,  # noqa: E501
                               sum_closure=lambda a, b: a[0] + b[0]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], [0, 3],  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[0], a[1] + b[1]],  # noqa: E501
                               same_closure=lambda a, b: a[0] == b[0] and a[1] == b[1]),  # noqa: E501
                         [[[-3, 0], [3, 3]], [[-2, 1], [2, 2]]])  # noqa: E501
        self.assertEqual(n_sum(2, [[-3, 0], [-2, 1], [2, 2], [3, 3], [8, 4], [-9, 5]], -5,  # noqa: E501
                               sum_closure=lambda a, b: [a[0] + b[1], a[1] + b[0]],  # noqa: E501
                               compare_closure=lambda a, b: -1 if a[0] < b else 1 if a[0] > b else 0),  # noqa: E501
                         [[[-9, 5], [8, 4]]])  # noqa: E501


if __name__ == '__main__':

    unittest.main()
