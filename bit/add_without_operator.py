"""
The following code adds two positive integers without using the '+' operator.
The code uses bitwise operations to add two numbers.

Input: 2 3
Output: 5
"""
import unittest


def add_bitwise_operator(x, y):

    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


class TestSuite(unittest.TestCase):

    def test_add_bitwise_operator(self):

        self.assertEqual(5432 + 97823, add_bitwise_operator(5432, 97823))
        self.assertEqual(0, add_bitwise_operator(0, 0))
        self.assertEqual(10, add_bitwise_operator(10, 0))
        self.assertEqual(10, add_bitwise_operator(0, 10))


if __name__ == '__main__':
    unittest.main()
