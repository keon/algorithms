"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        ans = []
        k = 0
        for str in strs:
            sstr = ''.join(sorted(str))
            if sstr not in d:
                d[sstr] = k
                k = k+1
                ans.append([])
                ans[-1].append(str)
            else:
                ans[d[sstr]].append(str)
        return ans
