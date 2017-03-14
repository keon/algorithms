"""
Given an array of integers, every element appears
twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
        i ^= num
    return i
