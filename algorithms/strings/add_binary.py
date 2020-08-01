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

def add_binary(a, b):
    '''
    Given two binary strings,
    return their sum both as a binary string
    and integer value
    '''
    s = ""
    sint =0
    c, i, j = 0, len(a)-1, len(b)-1
    zero = ord('0')
    r=1
    while (i >= 0 or j >= 0 or c == 1):
        if (i >= 0):
            c += ord(a[i]) - zero
            i -= 1
        if (j >= 0):
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s
        sint += r*(c%2)
        c //= 2 
        r*=2
    return s,sint



def add_binary(a, b):
    '''
    Given two binary no. as integers,
    return their sum both as a binary string
    and integer value
    '''
    s = ""
    sint =0
    c =0
    zero = ord('0')
    r=1
    while (a > 0 or b>0 or  c==1):
        if (a > 0):
            c += a%10
        if (b > 0):
            c += b%10
        s = chr(c %2 + zero) + s
        sint += r*(c%2)
        c//=2
        r*=2
        a//=10
        b//=10
        
    return s,sint
