"""
Given an array of integers, every element appears
twice except for one. Find that single one.

NOTE: This also works for finding a number occurring odd
      number of times, where all the other numbers appear
      even number of times.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
import unittest
import random


def single_number(nums):
    """
    Returns single number, if found.
    Else if all numbers appear twice, returns 0.
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
        i ^= num
    return i


class TestSuite(unittest.TestCase):

    def test_single_number(self):

        random.seed('test')

        self.assertEqual(0, single_number([1, 0, 2, 1, 2, 3, 3]))
        self.assertEqual(101, single_number([101]))

        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 2  # nums contains pairs of random integers
        nums.append(single)
        random.shuffle(nums)

        self.assertEqual(single, single_number(nums))


if __name__ == '__main__':

    unittest.main()
