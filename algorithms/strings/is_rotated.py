"""
Given two strings s1 and s2, determine if s2 is a rotated version of s1.
For example,
is_rotated("hello", "llohe") returns True
is_rotated("hello", "helol") returns False

accepts two strings
returns bool
Reference: https://leetcode.com/problems/rotate-string/description/
"""

def is_rotated(s1, s2):
    if len(s1) == len(s2):
        return s2 in s1 + s1
    else:
        return False

"""
Another solution: brutal force
Complexity: O(N^2)
"""
def is_rotated_v1(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True

    for c in range(len(s1)):
        if all(s1[(c + i) % len(s1)] == s2[i] for i in range(len(s1))):
            return True
    return False
