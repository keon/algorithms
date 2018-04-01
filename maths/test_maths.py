from base_conversion import int2base,base2int
from extended_gcd import extended_gcd
from gcd import gcd,lcm
import unittest


class TestBaseConversion (unittest.TestCase):
    """
    Test for the file base_conversion.py
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int2base(self):
        self.assertEqual("101",int2base(5,2))
        self.assertEqual("0",int2base(0,2))
        self.assertEqual("FF",int2base(255,16))
    def test_base2int(self):
        self.assertEqual(5,base2int("101",2))
        self.assertEqual(0,base2int("0",2))
        self.assertEqual(255,base2int("FF",16))


class TestExtendedGcd (unittest.TestCase):
    """[summary]
    Test for the file extended_gcd.py
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_extended_gcd(self):
        self.assertEqual((0,1,2),extended_gcd(8,2))
        self.assertEqual((0,1,17),extended_gcd(13,17))


class TestGcd (unittest.TestCase):
    """[summary]
    Test for the file gcd.py
    Arguments:
        unittest {[type]} -- [description]
    """

    def test_gcd(self):
        self.assertEqual(4,gcd(8,12))
        self.assertEqual(1,gcd(13,17))
    def test_lcm(self):
        self.assertEqual(24,lcm(8,12))


if __name__ == "__main__":
    unittest.main()