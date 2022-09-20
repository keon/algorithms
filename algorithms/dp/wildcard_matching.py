"""
wildcard mathing

Given an input string (s) and a pattern (p), implement wildcard pattern 
matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
Example:
    input: s = "aabbcddfer" , p = "**dd?er*"
    output = True 
    explanation: "**" matches with "aabbc", "dd" = "dd" , "?" = "f", 
                 "er" = "er" and "*" = blank space
Constraints:

    1. 0 <= s.length, p.length <= 2000
    2. s contains only lowercase English letters.
    3. p contains only lowercase English letters, '?' or '*'.

To run the test use isMatch function and it will return bool.
"""

# Returns nested lists by splitting pChars on *.
# pChars expected to contains a-z, ?, and *.
# Duplicate contiguous * chars are dropped.
def splitPatternOnWildcards(pChars: list[chr]) -> list[list[chr]]:
    wc = 0
    other = 0

    pTokenChars = []
    cur = []
    for pChar in pChars:
        if pChar == '*':
            wc += 1
            if len(cur) > 0:
                pTokenChars.append(cur)
                cur = []
        else:
            other += 1
            cur.append(pChar)
    if len(cur) > 0:
        pTokenChars.append(cur)

    # If pChars contained only * characters, return a single nested list with a single *
    if len(pTokenChars) == 0 and wc > 0 and other == 0:
        pTokenChars.append(['*'])

    return pTokenChars

def consumeEdgeAligned(left: bool, pChars, sChars):
    idx = 0 if left else -1

    while len(pChars) > 0 and len(sChars) > 0:
        if pChars[idx] == "*":
            break  #stopping point
        if pChars[idx] != "?" and pChars[idx] != sChars[idx]:
            return False
        else:
            sChars.pop(idx)
            pChars.pop(idx)

    return True

def indexOf(s, p):
    for i in range(0, len(s) - len(p)+1):
        m = True
        for j in range(0, len(p)):
            if p[j] != "?" and s[i+j] != p[j]:
                m = False
        if m:
            return i

    return -1

def popNFromHead(s, n):
    for i in range(0, n):
        s.pop(0)

def isMatch(s, p):
    star_count = p.count("*")
    if len(p) > 0 and len(s) == 0 and len(p) != star_count:
        return False
    elif len(p) == 0 and len(s) == 0:
        return True

    sChars = list(s)
    pChars = list(p)

    if not consumeEdgeAligned(True, pChars, sChars):
        return False
    if not consumeEdgeAligned(False, pChars, sChars):
        return False

    subPatterns = splitPatternOnWildcards(pChars)

    if len(subPatterns) == 0 and len(sChars) > 0:
        return False

    if len(subPatterns) > 0 and subPatterns[0][0] == "*":
        return True

    for pattern in subPatterns:
        idx = indexOf(sChars, pattern)
        if idx == -1:
            return False
        popNFromHead(sChars, idx + len(pattern))

    return True

#example test case
arr1 = "aabbcddfer"
arr2 = "**dd?er*"
print(f"The array 1 and array 2 is a match: {isMatch(arr1,arr2)} ")