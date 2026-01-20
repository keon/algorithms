from algorithms.strings import (
    swap_str,
)

import unittest

class Testswap_str(unittest.TestCase):
    def test_swap_str1(self):
        self.assertEqual(swap_str.checkSwapEquality('aabc','abcd'),True)

    def test_swap_str2(self):
        self.assertEqual(swap_str.checkSwapEquality('abcdef', 'fghijk'), True)

    def test_swap_str3(self):
        self.assertEqual(swap_str.checkSwapEquality('aab', 'c'), False)

    def test_swap_str4(self):
        self.assertEqual(swap_str.checkSwapEquality('mnopppq', 'xyzaa'), True)

if __name__ == '__main__':
    unittest.main()