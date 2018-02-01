# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.

def longest_non_repeat(string):
    if string is None:
        return 0
    temp = []
    max_len = 0
    for i in string:
        if i in temp:
            temp = []
        temp.append(i)
        max_len = max(max_len, len(temp))
    return max_len

def longest_non_repeat_two(string):
    if string is None:
        return 0
    start, max_len = 0, 0
    user_char = {}
    for index, char in enumerate(string):
        if char in user_char and start <= user_char[char]:
            start = user_char[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        user_char[char] = index
    return  max_len

if __name__ == '__main__':
    a = "abcabcdefbb"
    print(a)
    print(longest_non_repeat(a))
    print(longest_non_repeat_two(a))
