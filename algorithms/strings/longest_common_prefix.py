"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Reference: https://leetcode.com/problems/longest-common-prefix/description/
"""

"""
First solution: Horizontal scanning
"""
def common_prefix(s1, s2):
    "Return prefix common of 2 strings"
    if not s1 or not s2:
        return ""
    k = 0
    while s1[k] == s2[k]:
        k = k + 1
        if k >= len(s1) or k >= len(s2):
            return s1[0:k]
    return s1[0:k]

def longest_common_prefix_v1(strs):
    if not strs:
        return ""
    result = strs[0]
    for i in range(len(strs)):
        result = common_prefix(result, strs[i])
    return result

"""
Second solution: Vertical scanning
"""
def longest_common_prefix_v2(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i == len(string) or string[i] != strs[0][i]:
                return strs[0][0:i]
    return strs[0]

"""
Third solution: Divide and Conquer
"""
def longest_common_prefix_v3(strs):
    if not strs:
        return ""
    return longest_common(strs, 0, len(strs) -1)

def longest_common(strs, left, right):
    if left == right:
        return strs[left]
    mid = (left + right) // 2
    lcp_left = longest_common(strs, left, mid)
    lcp_right = longest_common(strs, mid + 1, right)
    return common_prefix(lcp_left, lcp_right)
