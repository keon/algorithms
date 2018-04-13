from add_bitwise_operator import add_bitwise_operator
from count_ones import count_ones_iter, count_ones_recur
from find_missing_number import find_missing_number, find_missing_number2
from power_of_two import is_power_of_two
from reverse_bits import reverse_bits
from single_number import single_number
from single_number2 import single_number2
from subsets import subsets

import unittest
import random

class TestSuite(unittest.TestCase):

    def test_add_bitwise_operator(self):
        self.assertEqual(5432 + 97823, add_bitwise_operator(5432, 97823))
        self.assertEqual(0, add_bitwise_operator(0, 0))
        self.assertEqual(10, add_bitwise_operator(10, 0))
        self.assertEqual(10, add_bitwise_operator(0, 10))

    def test_count_ones_recur(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_recur(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_recur(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_recur(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_recur(0))

    def test_count_ones_iter(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_iter(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_iter(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_iter(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_iter(0))

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

    def test_is_power_of_two(self):

        self.assertTrue(is_power_of_two(64))
        self.assertFalse(is_power_of_two(91))
        self.assertTrue(is_power_of_two(2**1001))
        self.assertTrue(is_power_of_two(1))
        self.assertFalse(is_power_of_two(0))


if __name__ == '__main__':
    unittest.main()
