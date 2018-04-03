"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary
representation 00000000000000000000000000001011,
so the function should return 3.
 
T(n)- O(k)   : k is the number of 1s present in binary representation.
NOTE: this complexity is better than O(log n). 
e.g. for n = 00010100000000000000000000000000
only 2 iterations are required.

Number of loops is
equal to the number of 1s in the binary representation."""
import unittest


def count_ones_recur(n):
    """Using Brian Kernighan’s Algorithm. (Recursive Approach)"""

    if not n:
        return 0
    return 1 + count_ones_recur(n & (n-1))


def count_ones_iter(n):
    """Using Brian Kernighan’s Algorithm. (Iterative Approach)"""

    count = 0
    while n:
        n &= (n-1) 
        count += 1
    return count


class TestSuite(unittest.TestCase):

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


if __name__ == '__main__':

    unittest.main()