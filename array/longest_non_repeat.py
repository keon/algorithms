# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.

def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i-start+1)
        used_char[char] = i
    return maxlen

a = "abcabcdefbb"
print(a)
print(longest_non_repeat(a))
