import unittest

from algorithms.data_structures.veb_tree import VEBTree


class TestVEBTree(unittest.TestCase):
    def setUp(self):
        self.veb = VEBTree(16)

    def test_insert_and_member(self):
        values = [2, 3, 4, 7, 14]
        for v in values:
            self.veb.insert(v)

        for v in values:
            self.assertTrue(self.veb.member(v))

        self.assertFalse(self.veb.member(5))

    def test_min_max(self):
        self.veb.insert(10)
        self.veb.insert(2)
        self.veb.insert(15)

        self.assertEqual(2, self.veb.minimum())
        self.assertEqual(15, self.veb.maximum())

    def test_successor(self):
        for v in [2, 4, 8, 12]:
            self.veb.insert(v)

        self.assertEqual(4, self.veb.successor(2))
        self.assertEqual(8, self.veb.successor(4))
        self.assertIsNone(self.veb.successor(12))

    def test_delete(self):
        for v in [1, 3, 5, 7]:
            self.veb.insert(v)

        self.veb.delete(3)
        self.assertFalse(self.veb.member(3))
        self.assertEqual(5, self.veb.successor(1))

    def test_invalid_universe(self):
        with self.assertRaises(ValueError):
            VEBTree(15)  # not power of 2


if __name__ == "__main__":
    unittest.main()
