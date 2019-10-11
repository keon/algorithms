"""
Integer base conversion algorithm

int2base(5, 2) return '101'.
base2int('F', 16) return 15.

"""

import string

def int_to_base(n, base):
    """
        :type n: int
        :type base: int
        :rtype: str
    """
    is_negative = False
    if n == 0:
        return '0'
    elif n < 0:
        is_negative = True
        n *= -1
    digit = string.digits + string.ascii_uppercase
    res = ''
    while n > 0:
        res += digit[n % base]
        n //= base
    if is_negative:
        return '-' + res[::-1]
    else:
        return res[::-1]


def base_to_int(s, base):
    """
        Note : You can use int() built-in function instread of this.
        :type s: str
        :type base: int
        :rtype: int
    """
    
    digit = {}
    for i,c in enumerate(string.digits + string.ascii_uppercase):
        digit[c] = i
    multiplier = 1
    res = 0
    for c in s[::-1]:
        res += digit[c] * multiplier
        multiplier *= base
    return res
