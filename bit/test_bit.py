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

    def test_reverse_bits(self):

        self.assertEqual(43261596, reverse_bits(964176192))
        self.assertEqual(964176192, reverse_bits(43261596))
        self.assertEqual(1, reverse_bits(2147483648))

        # bin(0) => 00000000000000000000000000000000
        self.assertEqual(0, reverse_bits(0))

        # bin(2**32 - 1) => 11111111111111111111111111111111
        self.assertEqual(2**32 - 1, reverse_bits(2**32 - 1))

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

    def test_single_number2(self):

        self.assertEqual(3, single_number2([4, 2, 3, 2, 1, 1, 4, 2, 4, 1]))
        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 3  # nums contains triplets of random integers
        nums.append(single)
        random.shuffle(nums)
        self.assertEqual(single, single_number2(nums))

    def test_subsets(self):

        self.assertSetEqual(subsets([1, 2, 3]),
                            {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)})

        self.assertSetEqual(subsets([10, 20, 30, 40]),
                            {(10, 40), (10, 20, 40), (10, 30), (10, 20, 30, 40), (40,),
                             (10, 30, 40), (30,), (20, 30), (30, 40), (10,), (),
                             (10, 20), (20, 40), (20, 30, 40), (10, 20, 30), (20,)})

if __name__ == '__main__':
    unittest.main()
