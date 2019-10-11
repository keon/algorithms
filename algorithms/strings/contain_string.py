"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Reference: https://leetcode.com/problems/implement-strstr/description/
"""
def contain_string(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if len(haystack) - i < len(needle):
            return -1
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
