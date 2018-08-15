"""
Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.

For example:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Reference: https://leetcode.com/problems/delete-operation-for-two-strings/description/
"""

def min_distance(word1, word2):
    return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2))

def lcs(s1, s2, i, j):
    """
    The length of longest common subsequence among the two given strings s1 and s2
    """
    if i == 0 or j == 0:
        return 0
    elif s1[i - 1] == s2[j - 1]:
        return 1 + lcs(s1, s2, i - 1, j - 1)
    else:
        return max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))

# TODO: Using dynamic programming
