"""
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lmin = lmax = gmax = nums[0]
    for i in range(len(nums)):
        t1 = nums[i] * lmax
        t2 = nums[i] * lmin
        lmax = max(max(t1, t2), nums[i])
        lmin = min(min(t1, t2), nums[i])
        gmax = max(gmax, lmax)
