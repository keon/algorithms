from algorithms.ml.nearest_neighbor import (
    distance,
    nearest_neighbor,
)

from algorithms.ml.linear_regression import (
    simple_linear_regression
)

import unittest


class TestML(unittest.TestCase):
    def setUp(self):
        # train set for the AND-function
        self.trainSetAND = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}

        # train set for light or dark colors

        self.data_set_linear_reg = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]]
        
        self.trainSetLight = {(11, 98, 237): 'L', (3, 39, 96): 'D',
                              (242, 226, 12): 'L', (99, 93, 4): 'D',
                              (232, 62, 32): 'L', (119, 28, 11): 'D',
                              (25, 214, 47): 'L', (89, 136, 247): 'L',
                              (21, 34, 63): 'D', (237, 99, 120): 'L',
                              (73, 33, 39): 'D'}

    def test_nearest_neighbor(self):
        # AND-function
        self.assertEqual(nearest_neighbor((1, 1), self.trainSetAND), 1)
        self.assertEqual(nearest_neighbor((0, 1), self.trainSetAND), 0)

        # dark/light color test

        self.assertEqual(nearest_neighbor((31, 242, 164),
                                          self.trainSetLight), 'L')
        self.assertEqual(nearest_neighbor((13, 94, 64),
                                          self.trainSetLight), 'D')
        self.assertEqual(nearest_neighbor((230, 52, 239),
                                          self.trainSetLight), 'L')

    def test_distance(self):
        self.assertAlmostEqual(distance((1, 2, 3), (1, 0, -1)), 4.47, 2)

    def test_linear_regression(self):
        param_0, param_1, rse, r_2 = simple_linear_regression(
            self.data_set_linear_reg)

        self.assertAlmostEqual(param_0, 1.2363636363636363)
        self.assertAlmostEqual(param_1, 1.1696969696969697)
        self.assertAlmostEqual(rse, 0.8384690232980003)
        self.assertAlmostEqual(r_2, 0.952538038613988)

if __name__ == "__main__":
    unittest.main()
