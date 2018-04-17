"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""
import collections


# Time complexity O(n^2)
def delete_nth_naive(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


# Time Complexity O(n), using hash tables.
def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)  # keep track of occurrences

    for i in array:

        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    return result
