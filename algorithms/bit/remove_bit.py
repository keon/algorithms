"""
Remove_bit(num, i): remove a bit at specific position.
For example:

Input: num = 10101 (21)
remove_bit(num, 2): output = 1001 (9)
remove_bit(num, 4): output = 101 (5)
remove_bit(num, 0): output = 1010 (10)
"""

def remove_bit(num, i):
    mask = num >> (i + 1)
    mask = mask << i
    right = ((1 << i) - 1) & num
    return mask | right
