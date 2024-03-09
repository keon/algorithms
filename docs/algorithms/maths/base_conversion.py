"""
Integer base conversion algorithm

int_to_base(5, 2) return '101'.
base_to_int('F', 16) return 15.

"""

import string

def int_to_base(num, base):
    """
        :type num: int
        :type base: int
        :rtype: str
    """
    is_negative = False
    if num == 0:
        return '0'
    if num < 0:
        is_negative = True
        num *= -1
    digit = string.digits + string.ascii_uppercase
    res = ''
    while num > 0:
        res += digit[num % base]
        num //= base
    if is_negative:
        return '-' + res[::-1]
    return res[::-1]


def base_to_int(str_to_convert, base):
    """
        Note : You can use int() built-in function instead of this.
        :type str_to_convert: str
        :type base: int
        :rtype: int
    """

    digit = {}
    for ind, char in enumerate(string.digits + string.ascii_uppercase):
        digit[char] = ind
    multiplier = 1
    res = 0
    for char in str_to_convert[::-1]:
        res += digit[char] * multiplier
        multiplier *= base
    return res
