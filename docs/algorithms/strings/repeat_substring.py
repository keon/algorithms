"""
Given a non-empty string check if it can be constructed by taking
a substring of it and appending multiple copies of the substring together.

For example:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Input: "aba"
Output: False

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times.

Reference: https://leetcode.com/problems/repeated-substring-pattern/description/
"""
def repeat_substring(s):
    """
    :type s: str
    :rtype: bool
    """
    str = (s + s)[1:-1]
    return s in str
