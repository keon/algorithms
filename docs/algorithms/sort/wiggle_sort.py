"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
"""
def wiggle_sort(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

if __name__ == "__main__":
    array = [3, 5, 2, 1, 6, 4]

    print(array)
    wiggle_sort(array)
    print(array)


