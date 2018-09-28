from algorithms.dp import (
    edit_distance
)


import unittest


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('food', 'money'), 4)
        self.assertEqual(edit_distance('horse', 'ros'), 3)


if __name__ == '__main__':
    unittest.main()
