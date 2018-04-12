from bubble_sort import bubble_sort
from comb_sort import comb_sort
from counting_sort import counting_sort

import unittest

class TestSuite(unittest.TestCase):
        def test_bubble_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             bubble_sort([1, 5, 65, 23, 57, 1232]))

        def test_comb_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             comb_sort([1, 5, 65, 23, 57, 1232]))

        def test_counting_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             counting_sort([1, 5, 65, 23, 57, 1232]))
            self.assertEqual([-1232, -65, -57, -23, -5, -1],
                             counting_sort([-1, -5, -65, -23, -57, -1232]))

if __name__ == "__main__":
    unittest.main()
