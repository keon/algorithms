"""
Given two strings, determine if they are equal after reordering.

Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in s1:
        pos = ord(c)-ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c)-ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2
