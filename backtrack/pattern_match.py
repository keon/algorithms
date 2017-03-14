"""
Given a pattern and a string str,
find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""


def pattern_match(pattern, string):
    """
    :type pattern: str
    :type string: str
    :rtype: bool
    """
    return backtrack(pattern, string, {})


def backtrack(pattern, string, dic):
    print(dic)
    if len(pattern) == 0 and len(string) > 0:
        return False
    if len(pattern) == len(string) == 0:
        return True
    for end in range(1, len(string)-len(pattern)+2):
        if pattern[0] not in dic and string[:end] not in dic.values():
            dic[pattern[0]] = string[:end]
            if backtrack(pattern[1:], string[end:], dic):
                return True
            del dic[pattern[0]]
        elif pattern[0] in dic and dic[pattern[0]] == string[:end]:
            if backtrack(pattern[1:], string[end:], dic):
                return True
    return False

if __name__ == "__main__":
    pattern1 = "abab"
    string1 = "redblueredblue"
    pattern2 = "aaaa"
    string2 = "asdasdasdasd"
    pattern3 = "aabb"
    string3 = "xyzabcxzyabc"
    print(pattern_match(pattern1, string1))
    print(pattern_match(pattern2, string2))
    print(pattern_match(pattern3, string3))
