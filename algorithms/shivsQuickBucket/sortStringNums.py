'''
Comparison Functions - functools.cmp_to_key
For example, a balance scale compares two samples giving a relative ordering: lighter, equal, or heavier. 
Likewise, a comparison function such as cmp(a, b) will return a negative value for less-than, zero if the inputs are equal, or a positive value for greater-than.
usage - 
sorted(words, key=cmp_to_key(strcoll))  # locale-aware sort order

Q - https://www.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1
'''

import functools
class Solution:
    def printLargest(self, n, arr):
        sarr = [str(num) for num in arr]

        def checkk(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        return ''.join(sorted(sarr, key=functools.cmp_to_key(checkk)))
