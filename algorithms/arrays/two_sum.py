"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""


def two_sum(array, target):
    for i, num in enumerate(zip(array, array[1:])):
        if num[0] + num[1] == target:
            return (i, i+1)
    return None
