from strings.add_binary import add_binary
from strings.breaking_bad import match_symbol, match_symbol_1, bracket
from strings.decode_string import decode_string
from strings.delete_reoccurring import delete_reoccurring_characters
from strings.domain_extractor import domain_name_1, domain_name_2
from strings.encode_decode import encode, decode
from strings.group_anagrams import group_anagrams
from strings.int_to_roman import int_to_roman

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
        self.assertEqual(('[Am]azon', 'Mi[cro]soft', 'Goog[le]'), bracket(self.words, self.symbols))


class TestDecodeString(unittest.TestCase):
    """[summary]
    Test for the file decode_string.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_decode_string(self):
        self.assertEqual("aaabcbc", decode_string("3[a]2[bc]"))
        self.assertEqual("accaccacc", decode_string("3[a2[c]]"))


class TestDeleteReoccurring(unittest.TestCase):
    """[summary]
    Test for the file delete_reoccurring.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_delete_reoccurring_characters(self):
        self.assertEqual("abc", delete_reoccurring_characters("aaabcccc"))


class TestDomainExtractor(unittest.TestCase):
    """[summary]
    Test for the file domain_extractor.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_valid(self):
        self.assertEqual(domain_name_1("https://github.com/SaadBenn"), "github")
    def test_invalid(self):
        self.assertEqual(domain_name_2("http://google.com"), "google")


class TestEncodeDecode(unittest.TestCase):
    """[summary]
    Test for the file encode_decode.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_encode(self):
        self.assertEqual("4:keon2:is7:awesome", encode("keon is awesome"))
    def test_decode(self):
        self.assertEqual(['keon', 'is', 'awesome'], decode("4:keon2:is7:awesome"))


class TestGroupAnagrams(unittest.TestCase):
    """[summary]
    Test for the file group_anagrams.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_group_anagrams(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], \
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


class TestIntToRoman(unittest.TestCase):
    """[summary]
    Test for the file int_to_roman.py
    
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int_to_roman(self):
        self.assertEqual("DCXLIV", int_to_roman(644))
        self.assertEqual("I", int_to_roman(1))
        self.assertEqual("MMMCMXCIX", int_to_roman(3999))


if __name__ == "__main__":
    unittest.main()