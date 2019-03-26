from algorithms.dp import (
    edit_distance,
    hosoya_triangle
)


import unittest


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('food', 'money'), 4)
        self.assertEqual(edit_distance('horse', 'ros'), 3)

class TestHosoyaTriangle(unittest.TestCase):
    """[summary]
    Test for the file hosoya_triangle
    
    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_hosoya(self):
        self.assertEqual([1], hosoya_triangle.hosoya_testing(1))
        self.assertEqual([1,
                         1, 1,
                         2, 1, 2,
                         3, 2, 2, 3,
                         5, 3, 4, 3, 5,
                         8, 5, 6, 6, 5, 8],
                         hosoya_triangle.hosoya_testing(6))
        self.assertEqual([1,
                          1, 1,
                          2, 1, 2,
                          3, 2, 2, 3,
                          5, 3, 4, 3, 5,
                          8, 5, 6, 6, 5, 8,
                          13, 8, 10, 9, 10, 8, 13,
                          21, 13, 16, 15, 15, 16, 13, 21,
                          34, 21, 26, 24, 25, 24, 26, 21, 34,
                          55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
                          hosoya_triangle.hosoya_testing(10))


if __name__ == '__main__':
    unittest.main()
