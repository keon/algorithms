from base_conversion import int2base,base2int
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


if __name__ == "__main__":
    unittest.main()