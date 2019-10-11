"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

For example:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Reference: https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""
def first_unique_char(s):
    """
    :type s: str
    :rtype: int
    """
    if (len(s) == 1):
        return 0
    ban = []
    for i in range(len(s)):
        if all(s[i] != s[k] for k in range(i + 1, len(s))) == True and s[i] not in ban:
            return i
        else:
            ban.append(s[i])
    return -1   
