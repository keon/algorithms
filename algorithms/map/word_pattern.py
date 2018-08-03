"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
Reference: https://leetcode.com/problems/word-pattern/description/
"""
def word_pattern(pattern, str):
    map = {}
    list_str = str.split()
    if len(list_str) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in map:
            if list_str[i] in map.values():
                return False
            map[pattern[i]] = list_str[i]
        else:
            if map[pattern[i]] != list_str[i]:
                return False
    return True
