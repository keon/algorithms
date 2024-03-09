"""
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that
add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

"""

DP = None

def helper_topdown(nums, target):
    """Generates DP and finds result.

    Keyword arguments:
    nums -- positive integer array without duplicates
    target -- integer describing what a valid combination should add to
    """
    if DP[target] != -1:
        return DP[target]
    res = 0
    for num in nums:
        if target >= num:
            res += helper_topdown(nums, target - num)
    DP[target] = res
    return res


def combination_sum_topdown(nums, target):
    """Find number of possible combinations in nums that add up to target, in top-down manner.

    Keyword arguments:
    nums -- positive integer array without duplicates
    target -- integer describing what a valid combination should add to
    """
    global DP
    DP = [-1] * (target + 1)
    DP[0] = 1
    return helper_topdown(nums, target)

def combination_sum_bottom_up(nums, target):
    """Find number of possible combinations in nums that add up to target, in bottom-up manner.

    Keyword arguments:
    nums -- positive integer array without duplicates
    target -- integer describing what a valid combination should add to
    """
    combs = [0] * (target + 1)
    combs[0] = 1
    for i in range(0, len(combs)):
        for num in nums:
            if i - num >= 0:
                combs[i] += combs[i - num]
    return combs[target]
