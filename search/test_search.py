from binary_search import binary_search, binary_search_recur
from first_occurance import first_occurance
from last_occurance import last_occurance
from search_insert import search_insert
from two_sum import two_sum, two_sum1, two_sum2
from search_range import search_range

import unittest

class TestSuite(unittest.TestCase):

    def test_first_occurance(self):
        def helper(array, query):
            idx = array.index(query) if query in array else None
            return idx
        array = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(first_occurance(array, 1), helper(array, 1))
        self.assertEqual(first_occurance(array, 3), helper(array, 3))
        self.assertEqual(first_occurance(array, 5), helper(array, 5))
        self.assertEqual(first_occurance(array, 6), helper(array, 6))
        self.assertEqual(first_occurance(array, 7), helper(array, 7))
        self.assertEqual(first_occurance(array, -1), helper(array, -1))

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

    def test_last_occurance(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(5, last_occurance(array, 3))
        self.assertEqual(10, last_occurance(array, 5))
        self.assertEqual(None, last_occurance(array, 7))
        self.assertEqual(0, last_occurance(array, 1))
        self.assertEqual(13, last_occurance(array, 6))

    def test_search_insert(self):
        array = [1,3,5,6]
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

if __name__ == '__main__':

    unittest.main()
