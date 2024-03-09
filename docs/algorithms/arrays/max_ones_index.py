"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.

e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""


def max_ones_index(arr):

    n = len(arr)
    max_count = 0
    max_index = 0
    prev_zero = -1
    prev_prev_zero = -1

    for curr in range(n):

        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if arr[curr] == 0:
            if curr - prev_prev_zero > max_count:
                max_count = curr - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_zero = curr

    if n - prev_prev_zero > max_count:
        max_index = prev_zero

    return max_index
