"""

https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)

"""
import unittest

def bubble_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_bubble_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         bubble_sort([1, 5, 65, 23, 57, 1232]))
if __name__ == "__main__":
    unittest.main()
