"""
Given an array and a number k
Find the max elements of each of its sub-arrays of length k.

Keep indexes of good candidates in deque d.
The indexes in d are from the current window, they're increasing,
and their corresponding nums are decreasing.
Then the first deque element is the index of the largest window value.

For each index i:

1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index i - k, if it's still in the deque
   (it falls out of the window).
4. If our window has reached size k,
   append the current window maximum to the output.
"""

import collections
import unittest


def max_sliding_window(arr, k):
    qi = collections.deque()  # queue storing indexes of elements
    result = []
    for i, n in enumerate(arr):
        while qi and arr[qi[-1]] < n:
            qi.pop()
        qi.append(i)
        if qi[0] == i - k:
            qi.popleft()
        if i >= k - 1:
            result.append(arr[qi[0]])
    return result


class TestSuite(unittest.TestCase):

    def test_max_sliding_window(self):

        array = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual(max_sliding_window(array, k=5), [5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=7), [6, 7])

        array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
        self.assertEqual(max_sliding_window(array, k=4), [10, 10, 10, 15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=7), [15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=2), [8, 10, 10, 9, 9, 15, 15, 90, 90])


if __name__ == '__main__':

    unittest.main()