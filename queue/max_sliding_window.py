import collections

# Keep indexes of good candidates in deque d.
# The indexes in d are from the current window, they're increasing,
# and their corresponding nums are decreasing.
# Then the first deque element is the index of the largest window value.

# For each index i:

# 1. Pop (from the end) indexes of smaller elements (they'll be useless).
# 2. Append the current index.
# 3. Pop (from the front) the index i - k, if it's still in the deque
#    (it falls out of the window).
# 4. If our window has reached size k,
#    append the current window maximum to the output.


def max_sliding_window(nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out


array = [1,3,-1,-3,5,3,6,7]

print(max_sliding_window(array))
