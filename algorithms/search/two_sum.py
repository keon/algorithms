"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number. The function two_sum
should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you
may not use the same element twice.

Input: numbers = [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2

Solution:
two_sum: using binary search
two_sum1: using dictionary as a hash table
two_sum2: using two pointers
"""
# Using binary search technique
def two_sum(numbers, target):
    for i in range(len(numbers)):
        second_val = target - numbers[i]
        low, high = i+1, len(numbers)-1
        while low <= high:
            mid = low + (high - low) // 2
            if second_val == numbers[mid]:
                return [i + 1, mid + 1]
            elif second_val > numbers[mid]:
                low = mid + 1
            else:
                high = mid - 1

# Using dictionary as a hash table
def two_sum1(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i

# Using two pointers
def two_sum2(numbers, target):
    p1 = 0                      # pointer 1 holds from left of array numbers
    p2 = len(numbers) - 1       # pointer 2 holds from right of array numbers
    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1 + 1, p2 + 1]
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 + 1
