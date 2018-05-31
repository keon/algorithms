"""
Swap_pair: A function swap odd and even bits in an integer with as few instructions
as possible (Ex bit and bit 1 are swapped, bit 2 and bit 3 are swapped)

For example:
22: 010110  --> 41: 101001
10: 1010    --> 5 : 0101
"""

"""
We can approach this as operating on the odds bit first, and then the even bits.
We can mask all odd bits with 10101010 in binary ('AA') then shift them right by 1
Similarly, we mask all even bit with 01010101 in binary ('55') then shift them left
by 1. Finally, we merge these two values by OR operation.
"""
def swap_pair(num):
    # odd bit arithmetic right shift 1 bit
    odd = (num & int('AAAAAAAA', 16)) >> 1
    # even bit left shift 1 bit
    even = (num & int('55555555', 16)) << 1
    return odd | even
