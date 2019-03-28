"""
    Returns the missing number from a sequence of unique integers
    in range [0..n] in O(n) time and space. The difference between
    consecutive integers cannot be more than 1. If the sequence is
    already complete, the next integer in the sequence will be returned.

    For example:
    Input: nums = [4, 1, 3, 0, 6, 5, 2]
    Output: 7
"""
def find_missing_number(nums):

    missing = 0
    for i, num in enumerate(nums):
        missing ^= num
        missing ^= i + 1

    return missing


def find_missing_number2(nums):

    num_sum = sum(nums)
    n = len(nums)
    total_sum = n*(n+1) // 2
    missing = total_sum - num_sum
    return missing
