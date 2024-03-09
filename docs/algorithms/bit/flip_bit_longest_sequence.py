"""
You have an integer and you can flip exactly one bit from a 0 to 1.
Write code to find the length of the longest sequence of 1s you could create.
For example:
Input: 1775 ( or: 11011101111)
Output: 8
"""


def flip_bit_longest_seq(num):

    curr_len = 0
    prev_len = 0
    max_len = 0

    while num:
        if num & 1 == 1:  # last digit is 1
            curr_len += 1

        elif num & 1 == 0:  # last digit is 0
            if num & 2 == 0:  # second last digit is 0
                prev_len = 0
            else:
                prev_len = curr_len
            curr_len = 0

        max_len = max(max_len, prev_len + curr_len)
        num = num >> 1  # right shift num

    return max_len + 1
