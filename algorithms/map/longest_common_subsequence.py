"""
Given string a and b, with b containing all distinct characters,
find the longest common sub sequence's length.

Expected complexity O(n logn).
"""


def max_common_sub_string(s1, s2):
    # Assuming s2 has all unique chars
    s2dic = {s2[i]: i for i in range(len(s2))}
    maxr = 0
    subs = ''
    i = 0
    while i < len(s1):
        if s1[i] in s2dic:
            j = s2dic[s1[i]]
            k = i
            while j < len(s2) and k < len(s1) and s1[k] == s2[j]:
                k += 1
                j += 1
            if k - i > maxr:
                maxr = k-i
                subs = s1[i:k]
            i = k
        else:
            i += 1
    return subs
