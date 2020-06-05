from algorithms.distribution.histogram import get_histogram

import unittest


class TestListsInHistogram(unittest.TestCase):
    def test_histogram(self):
        list_1 = [3, 3, 2, 1]
        list_2 = [2, 3, 5, 5, 5, 6, 4, 3, 7]

        self.assertEqual(get_histogram(list_1), {1: 1, 2: 1, 3: 2})
        self.assertEqual(get_histogram(list_2),
                         {2: 1, 3: 2, 4: 1, 5: 3, 6: 1, 7: 1})


if __name__ == '__main__':
    unittest.main()
