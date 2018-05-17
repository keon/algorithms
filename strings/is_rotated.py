"""
Given two strings s1 and s2, determine if s2 is a rotated version of s1.
For example,
is_rotated("hello", "llohe") returns True
is_rotated("hello", "helol") returns False

accepts two strings
returns bool
"""

def is_rotated(s1, s2):
    if len(s1) == len(s2):
        return s2 in s1 + s1
    else:
        return False