from bubble_sort import bubble_sort

import unittest

class TestSuite(unittest.TestCase):
        def test_bubble_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             bubble_sort([1, 5, 65, 23, 57, 1232]))

if __name__ == "__main__":
    unittest.main()
