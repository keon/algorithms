"""
Given string a and b, with b containing all distinct characters,
find the longest common subsequence's 

length. Expected complexity O(nlogn).
"""


def maxCommonSubString(S1,S2):
    ##Assuming S2 has all unique chars
    S2Dic = {S2[i]:i for i in xrange(len(S2))}
    maxR = 0
    subS = ''
    i = 0
    while i < len(S1):
        if S1[i] in S2Dic:
            j = S2Dic[S1[i]]
            k = i
            while j < len(S2) and k < len(S1) and S1[k] == S2[j]:
                k += 1
                j += 1
            if k - i > maxR:
               maxR = k-i
               subS = S1[i:k]
            i = k
        else:
            i += 1
    return subS
