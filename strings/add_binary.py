"""
Given two binary strings,
return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(a, b):
    s = ""
    c, i, j = 0, len(a)-1, len(b)-1
    zero = ord('0')
    while (i >= 0 or j >= 0 or c == 1):
        if (i >= 0):
            c += ord(a[i]) - zero
            i -= 1
        if (j >= 0):
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s
        c //= 2 
        
    return s
