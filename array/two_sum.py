"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
import unittest


def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None


class TestSuite(unittest.TestCase):

    def test_two_sum(self):

        self.assertTupleEqual((0, 2), two_sum([2, 11, 7, 9], target=9))
        self.assertTupleEqual((0, 3), two_sum([-3, 5, 2, 3, 8, -9], target=0))

        self.assertIsNone(two_sum([-3, 5, 2, 3, 8, -9], target=6))


if __name__ == "__main__":

    unittest.main()
