"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""


#
# Rotate the entire array 'k' times
# T(n)- O(nk)
#
def rotate_one_by_one(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(k):
        temp = nums[n-1]
        for j in range(n-1, 0, -1):
            nums[j] = nums[j-1]
        nums[0] = temp


#
# Reverse segments of the array, followed by the entire array
# T(n)- O(n)
#
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


def reverse(array, a, b):
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1
