"""
Given two strings text and pattern,
return the list of  start indexes in text that matches with the pattern
using knuth_morris_pratt algorithm.
If idx is in the list, text[idx : idx + M] matches with pattern.
Time complexity : O(N+M)
N and M is the length of text and pattern, respectively.
"""

def knuth_morris_pratt(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = [0 for i in range(m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret
