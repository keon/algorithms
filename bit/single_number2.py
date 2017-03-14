"""
Given an array of integers, every element appears
three times except for one, which appears exactly once.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


"""
32 bits for each integer.
Consider 1 bit in it, the sum of each integer's corresponding bit
(except for the single number)
should be 0 if mod by 3. Hence, we sum the bits of all
integers and mod by 3,
the remaining should be the exact bit of the single number.
In this way, you get the 32 bits of the single number.
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in range(0, 32):
        count = 0
        for num in nums:
            if ((num >> i) & 1):
                count += 1
        res |= ((count % 3) << i)
    if res >= 2**31:
        res -= 2**32
    return res


# Another awesome answer
def single_number2(nums):
    ones, twos = 0, 0
    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    return ones
