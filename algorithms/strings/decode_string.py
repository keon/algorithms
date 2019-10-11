# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

def decode_string(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []; cur_num = 0; cur_string = ''
    for c in s:
        if c == '[':
            stack.append((cur_string, cur_num))
            cur_string = ''
            cur_num = 0
        elif c == ']':
            prev_string, num = stack.pop()
            cur_string = prev_string + num * cur_string
        elif c.isdigit():
            cur_num = cur_num*10 + int(c)
        else:
            cur_string += c
    return cur_string
