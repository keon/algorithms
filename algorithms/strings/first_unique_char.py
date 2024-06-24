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

branch_coverage = {
    "branch_26": False,
    "branch_27": False,
    "branch_28": False,
    "branch_29": False,
    "branch_30": False,
}

def first_unique_char(s):
    """
    :type s: str
    :rtype: int
    """
    if (len(s) == 1):
        branch_coverage["branch_26"] = True
        return 0
    ban = []
    for i in range(len(s)):
        branch_coverage["branch_27"] = True
        if all(s[i] != s[k] for k in range(i + 1, len(s))) == True and s[i] not in ban:
            branch_coverage["branch_28"] = True
            return i
        else:
            branch_coverage["branch_29"] = True
            ban.append(s[i])
    branch_coverage["branch_30"] = True
    return -1   

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        
first_unique_char("leetcode")
first_unique_char("loveleetcode")
print_coverage()
