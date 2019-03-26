from algorithms.matrix import (
    crout_matrix_decomposition
    )


import unittest


class TestCroutMatrixDecomposition(unittest.TestCase):
    """[summary]
    Test for the file crout_matrix_decomposition.crout_matrix_decomposition.py

    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_crout_matrix_decomposition(self):
        self.assertEqual(([[9.0, 0.0], [7.0, 0.0]],
                          [[1.0, 1.0], [0.0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[9,9], [7,7]]))
                         
        self.assertEqual(([[1.0, 0.0, 0.0],
                           [3.0, -2.0, 0.0],
                           [6.0, -5.0, 0.0]],
                           [[1.0, 2.0, 3.0],
                            [0.0, 1.0, 2.0],
                            [0.0, 0.0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[1,2,3],[3,4,5],[6,7,8]]))
                         
        self.assertEqual(([[2.0, 0, 0, 0],
                           [4.0, -1.0, 0, 0],
                           [6.0, -2.0, 2.0, 0],
                           [8.0, -3.0, 3.0, 0.0]],
                          [[1.0, 0.5, 1.5, 0.5],
                           [0, 1.0, 2.0, 1.0],
                           [0, 0, 1.0, 0.0],
                           [0, 0, 0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[2,1,3,1], [4,1,4,1], [6,1,7,1], [8,1,9,1]]))
                           
    
        
if __name__ == "__main__":
    unittest.main()
