"""
Write a function to determine the number of bits you would need to
flip to convert integer A to integer B.
For example:
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""


def count_flips_to_convert(a, b):

    diff = a ^ b

    # count number of ones in diff
    count = 0
    while diff:
        diff &= (diff - 1)
        count += 1
    return count
