"""
A message containing letters from A-Z is being
encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits,
determine the total number of ways to decode it.

For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


def num_decodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s[0] == "0":
        return 0
    wo_last, wo_last_two = 1, 1
    for i in range(1, len(s)):
        x = wo_last if s[i] != "0" else 0
        y = wo_last_two if int(s[i-1:i+1]) < 27 and s[i-1] != "0" else 0
        wo_last_two = wo_last
        wo_last = x+y
    return wo_last


def num_decodings2(s):
    if not s or s.startswith('0'):
        return 0
    stack = [1, 1]
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i-1] == '0' or s[i-1] > '2':
                # only '10', '20' is valid
                return 0
            stack.append(stack[-2])
        elif 9 < int(s[i-1:i+1]) < 27:
            # '01 - 09' is not allowed
            stack.append(stack[-2]+stack[-1])
        else:
            # other case '01, 09, 27'
            stack.append(stack[-1])
    return stack[-1]
