from strings.add_binary import add_binary
from strings.breaking_bad import match_symbol, match_symbol_1, bracket

import unittest


class TestAddBinary(unittest.TestCase):
    """[summary]
    Test for the file add_binary.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_add_binary(self):
        self.assertEqual("100", add_binary("11", "1"))
        self.assertEqual("101", add_binary("100", "1"))
        self.assertEqual("10", add_binary("1", "1"))


class TestBreakingBad(unittest.TestCase):
    """[summary]
    Test for the file breaking_bad.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        self.words = ['Amazon', 'Microsoft', 'Google']
        self.symbols = ['i', 'Am', 'cro', 'le', 'abc']
        self.result = ['M[i]crosoft', '[Am]azon', 'Mi[cro]soft', 'Goog[le]']
    def test_match_symbol(self):
        self.assertEqual(self.result, match_symbol(self.words,self.symbols))
    def test_match_symbol_1(self):
        self.assertEqual(['[Am]azon', 'Mi[cro]soft', 'Goog[le]'], match_symbol_1(self.words,self.symbols))
    def test_bracket(self):
        self.assertEqual(('[Am]azon', 'Mi[cro]soft', 'Goog[le]'),bracket(self.words, self.symbols))

if __name__ == "__main__":
    unittest.main()