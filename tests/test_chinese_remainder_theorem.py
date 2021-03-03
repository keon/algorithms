from algorithms.maths import chinese_remainder_theorem as crt
import unittest

class TestChineseRemainderSolver(unittest.TestCase):
    def test_k_three(self):
        # Example which should give the answer 143 
        # which is the smallest possible x that
        # solves the system of equations
        num = [3, 7, 10]
        rem = [2, 3, 3]
        self.assertEqual(crt.solve_chinese_remainder(num, rem), 143)

    def test_k_five(self):
        # Example which should give the answer 3383 
        # which is the smallest possible x that
        # solves the system of equations
        num = [3, 5, 7, 11, 26]
        rem = [2, 3, 2, 6, 3]
        self.assertEqual(crt.solve_chinese_remainder(num, rem), 3383)

    def test_exception_non_coprime(self):
        # There should be an exception when all
        # numbers in num are not pairwise coprime
        num = [3, 7, 10, 14]
        rem = [2, 3, 3, 1]
        with self.assertRaises(Exception):
            crt.solve_chinese_remainder(num, rem)
    
    def test_empty_lists(self):
        num = []
        rem = []
        with self.assertRaises(Exception):
            crt.solve_chinese_remainder(num, rem)
