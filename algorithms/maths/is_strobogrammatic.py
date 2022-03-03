"""
A strobogrammatic number is a number that looks
the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""


def is_strobogrammatic(num):
    """
    :type num: str
    :rtype: bool
    """
    comb = "00 11 88 69 96"
    i = 0
    j = len(num) - 1
    while i <= j:
        if comb.find(num[i]+num[j]) == -1:
            return False
        i += 1
        j -= 1
    return True


def is_strobogrammatic2(num: str):
    """Another implementation."""
    return num == num[::-1].replace('6', '#').replace('9', '6').replace('#', '9')
