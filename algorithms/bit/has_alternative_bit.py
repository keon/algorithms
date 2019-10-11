"""
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.

For example:
Input: 5
Output: True because the binary representation of 5 is: 101.

Input: 7
Output: False because the binary representation of 7 is: 111.

Input: 11
Output: False because the binary representation of 11 is: 1011.

Input: 10
Output: True because The binary representation of 10 is: 1010.
"""

# Time Complexity - O(number of bits in n)
def has_alternative_bit(n):
    first_bit = 0
    second_bit = 0
    while n:
        first_bit = n & 1
        if n >> 1:
            second_bit = (n >> 1) & 1
            if not first_bit ^ second_bit:
                return False
        else:
            return True
        n = n >> 1
    return True    

# Time Complexity - O(1)
def has_alternative_bit_fast(n):
    mask1 = int('aaaaaaaa', 16)  # for bits ending with zero (...1010)
    mask2 = int('55555555', 16)  # for bits ending with one  (...0101)
    return mask1 == (n + (n ^ mask1)) or mask2 == (n + (n ^ mask2))
