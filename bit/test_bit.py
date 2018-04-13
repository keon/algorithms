from add_bitwise_operator import add_bitwise_operator
from count_ones import count_ones_iter, count_ones_recur
from find_missing_number import find_missing_number
from power_of_two import is_power_of_two
from reverse_bits import reverse_bits
from single_number import single_number
from single_number2 import single_number2
from subsets import subsets

import unittest


class TestSuite(unittest.TestCase):

    def test_add_bitwise_operator(self):
        self.assertEqual(5432 + 97823, add_bitwise_operator(5432, 97823))
        self.assertEqual(0, add_bitwise_operator(0, 0))
        self.assertEqual(10, add_bitwise_operator(10, 0))
        self.assertEqual(10, add_bitwise_operator(0, 10))

if __name__ == '__main__':
    unittest.main()
