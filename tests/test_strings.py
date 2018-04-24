from strings.add_binary import add_binary

import unittest

class TestAddBinary(unittest.TestCase):
    """[summary]
    Test for the file add_binary.py

    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_add_binary(self):
        self.assertEqual("100",add_binary("11","1"))
        self.assertEqual("101",add_binary("100","1"))
        self.assertEqual("10",add_binary("1","1"))

if __name__ == "__main__":
    unittest.main()