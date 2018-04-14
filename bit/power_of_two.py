"""
given an integer, write a function to determine if it is a power of two
"""
def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and not n & (n-1)
