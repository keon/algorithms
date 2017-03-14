"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


def summary_ranges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    res = []
    if len(nums) == 1:
        return [str(nums[0])]
    i = 0
    while i < len(nums):
        num = nums[i]
        while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
            i += 1
        if nums[i] != num:
            res.append(str(num) + "->" + str(nums[i]))
        else:
            res.append(str(num))
        i += 1
    return res
