"""
    Returns the missing number from a sequence of unique integers
    in range [0..n] in O(n) time and space. The difference between
    consecutive integers cannot be more than 1. If the sequence is
    already complete, the next integer in the sequence will be returned.
"""
import unittest
import random


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


class TestSuite(unittest.TestCase):

    def setUp(self):
        """Initialize seed."""
        random.seed("test")

    def test_find_missing_number(self):

        self.assertEqual(7, find_missing_number([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number([1]))
        self.assertEqual(1, find_missing_number([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number(nums))

    def test_find_missing_number2(self):

        self.assertEqual(7, find_missing_number2([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number2([1]))
        self.assertEqual(1, find_missing_number2([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number2(nums))


if __name__ == '__main__':

    unittest.main()
