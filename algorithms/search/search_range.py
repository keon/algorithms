
import math

def binary_search_leftmost(nums, target):

    low = 0
    high = len(nums) - 1

    while low != high:

        mid = math.floor((low + high) / 2)

        # Element not found
        if low > high:
            return -1
        
        # Element found, but... check whether there exists a leftmost element
        if target == nums[mid]:
            high = mid

        # Shrinken the array
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    
    # Final check whether the element is correct
    if nums[low] == target:
        return low
    else:
        return -1

def binary_search_rightmost(nums, target):

    low = 0
    high = len(nums) - 1

    while low != high:

        mid = math.ceil((low + high) / 2)

        # Element not found
        if low > high:
            return -1
        
        # Element found, but... check whether there exists a rightmost element
        if target == nums[mid]:
            low = mid

        # Shrinken the array
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    
    # Final check whether the element is correct
    if nums[low] == target:
        return low
    else:
        return -1

"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value. If the target is not found in the
array, return [-1, -1].

For example:
Input: nums = [5,7,7,8,8,8,10], target = 8
Output: [3,5]
Input: nums = [5,7,7,8,8,8,10], target = 11
Output: [-1,-1]
"""
def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    leftSearch = binary_search_leftmost(nums, target)
    rightSearch = binary_search_rightmost(nums, target)

    # Element is there
    if leftSearch != -1:
        result = [leftSearch, rightSearch]
        return result

    # Element is not there
    else:
        return [-1, -1]
