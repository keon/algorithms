from algorithms.search import (
    binary_search, binary_search_recur,
    ternary_search,
    first_occurrence,
    last_occurrence,
    linear_search,
    search_insert,
    two_sum, two_sum1, two_sum2,
    search_range,
    find_min_rotate, find_min_rotate_recur,
    search_rotate, search_rotate_recur,
    jump_search,
    next_greatest_letter, next_greatest_letter_v1, next_greatest_letter_v2,
    interpolation_search
)

import unittest


class TestSuite(unittest.TestCase):

    def test_first_occurrence(self):
        def helper(array, query):
            idx = array.index(query) if query in array else None
            return idx
        array = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(first_occurrence(array, 1), helper(array, 1))
        self.assertEqual(first_occurrence(array, 3), helper(array, 3))
        self.assertEqual(first_occurrence(array, 5), helper(array, 5))
        self.assertEqual(first_occurrence(array, 6), helper(array, 6))
        self.assertEqual(first_occurrence(array, 7), helper(array, 7))
        self.assertEqual(first_occurrence(array, -1), helper(array, -1))

    def test_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, binary_search(array, 5))
        self.assertEqual(11, binary_search(array, 6))
        self.assertEqual(None, binary_search(array, 7))
        self.assertEqual(None, binary_search(array, -1))
        # Test binary_search_recur
        self.assertEqual(10, binary_search_recur(array, 0, 11, 5))
        self.assertEqual(11, binary_search_recur(array, 0, 11, 6))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, 7))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, -1))
    
    def test_ternary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, ternary_search(0, 11, 5, array))
        self.assertEqual(3, ternary_search(0, 10, 3, array))
        self.assertEqual(-1, ternary_search(0, 10, 5, array))
        self.assertEqual(-1, ternary_search(0, 11, 7, array))
        self.assertEqual(-1, ternary_search(0, 11, -1, array))
        

    def test_last_occurrence(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(5, last_occurrence(array, 3))
        self.assertEqual(10, last_occurrence(array, 5))
        self.assertEqual(None, last_occurrence(array, 7))
        self.assertEqual(0, last_occurrence(array, 1))
        self.assertEqual(13, last_occurrence(array, 6))

    def test_linear_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(6, linear_search(array, 4))
        self.assertEqual(10, linear_search(array, 5))
        self.assertEqual(-1, linear_search(array, 7))
        self.assertEqual(-1, linear_search(array, -1))

    def test_search_insert(self):
        array = [1, 3, 5, 6]
        self.assertEqual(2, search_insert(array, 5))
        self.assertEqual(1, search_insert(array, 2))
        self.assertEqual(4, search_insert(array, 7))
        self.assertEqual(0, search_insert(array, 0))

    def test_two_sum(self):
        array = [2, 7, 11, 15]
        # test two_sum
        self.assertEqual([1, 2], two_sum(array, 9))
        self.assertEqual([2, 4], two_sum(array, 22))
        # test two_sum1
        self.assertEqual([1, 2], two_sum1(array, 9))
        self.assertEqual([2, 4], two_sum1(array, 22))
        # test two_sum2
        self.assertEqual([1, 2], two_sum2(array, 9))
        self.assertEqual([2, 4], two_sum2(array, 22))

    def test_search_range(self):
        array = [5, 7, 7, 8, 8, 8, 10]
        self.assertEqual([3, 5], search_range(array, 8))
        self.assertEqual([1, 2], search_range(array, 7))
        self.assertEqual([-1, -1], search_range(array, 11))

    def test_find_min_rotate(self):
        array = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(0, find_min_rotate(array))
        array = [10, 20, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(-1, find_min_rotate(array))
        # Test find min using recursion
        array = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(0, find_min_rotate_recur(array, 0, 6))
        array = [10, 20, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(-1, find_min_rotate_recur(array, 0, 8))

    def test_search_rotate(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(8, search_rotate(array, 5))
        self.assertEqual(-1, search_rotate(array, 9))
        self.assertEqual(8, search_rotate_recur(array, 0, 11, 5))
        self.assertEqual(-1, search_rotate_recur(array, 0, 11, 9))

    def test_jump_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, jump_search(array, 5))
        self.assertEqual(2, jump_search(array, 3))
        self.assertEqual(-1, jump_search(array, 7))
        self.assertEqual(-1, jump_search(array, -1))

    def test_next_greatest_letter(self):
        letters = ["c", "f", "j"]
        target = "a"
        self.assertEqual("c", next_greatest_letter(letters, target))
        self.assertEqual("c", next_greatest_letter_v1(letters, target))
        self.assertEqual("c", next_greatest_letter_v2(letters, target))
        letters = ["c", "f", "j"]
        target = "d"
        self.assertEqual("f", next_greatest_letter(letters, target))
        self.assertEqual("f", next_greatest_letter_v1(letters, target))
        self.assertEqual("f", next_greatest_letter_v2(letters, target))
        letters = ["c", "f", "j"]
        target = "j"
        self.assertEqual("c", next_greatest_letter(letters, target))
        self.assertEqual("c", next_greatest_letter_v1(letters, target))
        self.assertEqual("c", next_greatest_letter_v2(letters, target))

    def test_interpolation_search(self):
        array = [0, 3, 5, 5, 9, 12, 12, 15, 16, 19, 20]
        self.assertEqual(1, interpolation_search(array, 3))
        self.assertEqual(2, interpolation_search(array, 5))
        self.assertEqual(6, interpolation_search(array, 12))
        self.assertEqual(-1, interpolation_search(array, 22))
        self.assertEqual(-1, interpolation_search(array, -10))
        self.assertEqual(10, interpolation_search(array, 20))


if __name__ == '__main__':

    unittest.main()
