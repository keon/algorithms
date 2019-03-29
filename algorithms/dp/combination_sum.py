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

dp = None


def helper_topdown(nums, target):
    global dp
    if dp[target] != -1:
        return dp[target]
    res = 0
    for i in range(0, len(nums)):
        if target >= nums[i]:
            res += helper_topdown(nums, target - nums[i])
    dp[target] = res
    return res


def combination_sum_topdown(nums, target):
    global dp
    dp = [-1] * (target + 1)
    dp[0] = 1
    return helper_topdown(nums, target)


# EDIT: The above solution is top-down. How about a bottom-up one?
def combination_sum_bottom_up(nums, target):
    comb = [0] * (target + 1)
    comb[0] = 1
    for i in range(0, len(comb)):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                comb[i] += comb[i - nums[j]]
    return comb[target]
