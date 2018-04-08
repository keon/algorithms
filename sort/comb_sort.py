"""

https://en.wikipedia.org/wiki/Comb_sort

Worst-case performance: O(N^2)

"""
import unittest
from math import floor


def comb_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(floor(gap/shrink))
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                sorted = False
            i = i + 1
    return arr

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_comb_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         comb_sort([1, 5, 65, 23, 57, 1232]))
if __name__ == "__main__":
    unittest.main()
