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
