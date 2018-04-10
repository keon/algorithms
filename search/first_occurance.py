#
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n)- O(log n)
#

import unittest

def firstOccurance(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        #print("lo: ", lo, " hi: ", hi, " mid: ", mid)
        if lo == hi:
            break
        if array[mid] < query:
            lo = mid + 1
        else:
            hi = mid
    if array[lo] == query:
      return lo

class TestSuite(unittest.TestCase):

    def test_firstOccurance(self):
        def helper(array, query):
            idx = array.index(query) if query in array else None
            return idx
        array = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(firstOccurance(array, 1), helper(array, 1))
        self.assertEqual(firstOccurance(array, 3), helper(array, 3))
        self.assertEqual(firstOccurance(array, 5), helper(array, 5))
        self.assertEqual(firstOccurance(array, 6), helper(array, 6))
        self.assertEqual(firstOccurance(array, 7), helper(array, 7))
        self.assertEqual(firstOccurance(array, -1), helper(array, -1))


if __name__ == '__main__':

    unittest.main()
