from algorithms.matrix import (
    bomb_enemy,
    copy_transform,
    crout_matrix_decomposition,
    cholesky_matrix_decomposition,
    matrix_exponentiation,
    matrix_inversion,
    multiply,
    rotate_image,
    sparse_dot_vector,
    spiral_traversal,
    sudoku_validator,
    sum_sub_squares,
    sort_matrix_diagonally
)
import unittest


class TestBombEnemy(unittest.TestCase):
    def test_3x4(self):
        grid1 = [
            ["0", "E", "0", "0"],
            ["E", "0", "W", "E"],
            ["0", "E", "0", "0"]
        ]
        self.assertEqual(3, bomb_enemy.max_killed_enemies(grid1))

        grid1 = [
            ["0", "E", "0", "E"],
            ["E", "E", "E", "0"],
            ["E", "0", "W", "E"],
            ["0", "E", "0", "0"]
        ]
        grid2 = [
            ["0", "0", "0", "E"],
            ["E", "0", "0", "0"],
            ["E", "0", "W", "E"],
            ["0", "E", "0", "0"]
        ]
        self.assertEqual(5, bomb_enemy.max_killed_enemies(grid1))
        self.assertEqual(3, bomb_enemy.max_killed_enemies(grid2))


class TestCopyTransform(unittest.TestCase):
    """[summary]
    Test for the file copy_transform.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_copy_transform(self):
        self.assertEqual(copy_transform.rotate_clockwise(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

        self.assertEqual(copy_transform.rotate_counterclockwise(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3, 6, 9], [2, 5, 8], [1, 4, 7]])

        self.assertEqual(copy_transform.top_left_invert(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

        self.assertEqual(copy_transform.bottom_left_invert(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[9, 6, 3], [8, 5, 2], [7, 4, 1]])


class TestCroutMatrixDecomposition(unittest.TestCase):
    """[summary]
    Test for the file crout_matrix_decomposition.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_crout_matrix_decomposition(self):
        self.assertEqual(([[9.0, 0.0], [7.0, 0.0]],
                          [[1.0, 1.0], [0.0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[9, 9], [7, 7]]))

        self.assertEqual(([[1.0, 0.0, 0.0],
                           [3.0, -2.0, 0.0],
                           [6.0, -5.0, 0.0]],
                          [[1.0, 2.0, 3.0],
                           [0.0, 1.0, 2.0],
                           [0.0, 0.0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[1, 2, 3], [3, 4, 5], [6, 7, 8]]))

        self.assertEqual(([[2.0, 0, 0, 0],
                           [4.0, -1.0, 0, 0],
                           [6.0, -2.0, 2.0, 0],
                           [8.0, -3.0, 3.0, 0.0]],
                          [[1.0, 0.5, 1.5, 0.5],
                           [0, 1.0, 2.0, 1.0],
                           [0, 0, 1.0, 0.0],
                           [0, 0, 0, 1.0]]),
                         crout_matrix_decomposition.crout_matrix_decomposition(
                             [[2, 1, 3, 1], [4, 1, 4, 1], [6, 1, 7, 1], [8, 1, 9, 1]]))


class TestCholeskyMatrixDecomposition(unittest.TestCase):
    """[summary]
    Test for the file cholesky_matrix_decomposition.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_cholesky_matrix_decomposition(self):
        self.assertEqual([[2.0, 0.0, 0.0],
                          [6.0, 1.0, 0.0],
                          [-8.0, 5.0, 3.0]],
                         cholesky_matrix_decomposition.cholesky_decomposition(
                             [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]))

        self.assertEqual(None,
                         cholesky_matrix_decomposition.cholesky_decomposition(
                             [[4, 12, -8], [12, 4, -43], [-16, -1, 32]]))

        self.assertEqual(None,
                         cholesky_matrix_decomposition.cholesky_decomposition(
                             [[4, 12, -16], [12, 37, -43], [-16, -43, 98], [1, 2, 3]]))

        # example taken from https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/04LinearAlgebra/cholesky/
        self.assertEqual([[2.23606797749979, 0.0, 0.0, 0.0],
                          [0.5366563145999494, 2.389979079406345, 0.0, 0.0],
                          [0.13416407864998736, -0.19749126846635062,
                              2.818332343581848, 0.0],
                          [-0.2683281572999747, 0.43682390737048743, 0.64657701271919, 3.052723872310221]],
                         cholesky_matrix_decomposition.cholesky_decomposition(
                             [[5, 1.2, 0.3, -0.6], [1.2, 6, -0.4, 0.9],
                              [0.3, -0.4, 8, 1.7], [-0.6, 0.9, 1.7, 10]]))


class TestInversion(unittest.TestCase):
    """[summary]
    Test for the file matrix_inversion.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_inversion(self):
        from fractions import Fraction

        m1 = [[1, 1], [1, 2]]
        self.assertEqual(matrix_inversion.invert_matrix(m1),
                         [[2, -1], [-1, 1]])

        m2 = [[1, 2], [3, 4, 5]]
        self.assertEqual(matrix_inversion.invert_matrix(m2), [[-1]])

        m3 = [[1, 1, 1, 1], [2, 2, 2, 2]]
        self.assertEqual(matrix_inversion.invert_matrix(m3), [[-2]])

        m4 = [[1]]
        self.assertEqual(matrix_inversion.invert_matrix(m4), [[-3]])

        m5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(matrix_inversion.invert_matrix(m5), [[-4]])

        m6 = [[3, 5, 1], [2, 5, 0], [1, 9, 8]]
        self.assertEqual(matrix_inversion.invert_matrix(m6), [[Fraction(40, 53), Fraction(-31, 53), Fraction(-5, 53)],
                                                              [Fraction(-16, 53), Fraction(
                                                                  23, 53), Fraction(2, 53)],
                                                              [Fraction(13, 53), Fraction(-22, 53), Fraction(5, 53)]])



class TestMatrixExponentiation(unittest.TestCase):
    """[summary]
    Test for the file matrix_exponentiation.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_matrix_exponentiation(self):
        mat = [[1, 0, 2], [2, 1, 0], [0, 2, 1]]

        self.assertEqual(matrix_exponentiation.matrix_exponentiation(mat, 0),
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        self.assertEqual(matrix_exponentiation.matrix_exponentiation(mat, 1),
            [[1, 0, 2], [2, 1, 0], [0, 2, 1]])

        self.assertEqual(matrix_exponentiation.matrix_exponentiation(mat, 2),
            [[1, 4, 4], [4, 1, 4], [4, 4, 1]])

        self.assertEqual(matrix_exponentiation.matrix_exponentiation(mat, 5),
            [[81, 72, 90], [90, 81, 72], [72, 90, 81]])


class TestMultiply(unittest.TestCase):
    """[summary]
    Test for the file multiply.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_multiply(self):
        self.assertEqual(multiply.multiply(
            [[1, 2, 3], [2, 1, 1]], [[1], [2], [3]]), [[14], [7]])


class TestRotateImage(unittest.TestCase):
    """[summary]
    Test for the file rotate_image.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_rotate_image(self):
        self.assertEqual(rotate_image.rotate(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])


class TestSparseDotVector(unittest.TestCase):
    """[summary]
    Test for the file sparse_dot_vector.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_sparse_dot_vector(self):
        self.assertEqual(sparse_dot_vector.dot_product(sparse_dot_vector.vector_to_index_value_list(
            [1., 2., 3.]), sparse_dot_vector.vector_to_index_value_list([0., 2., 2.])), 10)


class TestSpiralTraversal(unittest.TestCase):
    """[summary]
    Test for the file spiral_traversal.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_spiral_traversal(self):
        self.assertEqual(spiral_traversal.spiral_traversal(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])


class TestSudokuValidator(unittest.TestCase):
    """[summary]
    Test for the file sudoku_validator.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_sudoku_validator(self):
        self.assertTrue(
            sudoku_validator.valid_solution(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertTrue(
            sudoku_validator.valid_solution_hashtable(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertTrue(
            sudoku_validator.valid_solution_set(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution_hashtable(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution_set(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))


class TestSumSubSquares(unittest.TestCase):
    """[summary]
    Test for the file sum_sub_squares.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_sum_sub_squares(self):
        mat = [[1, 1, 1, 1, 1],
               [2, 2, 2, 2, 2],
               [3, 3, 3, 3, 3],
               [4, 4, 4, 4, 4],
               [5, 5, 5, 5, 5]]
        self.assertEqual(sum_sub_squares.sum_sub_squares(mat, 3),
                         [[18, 18, 18], [27, 27, 27], [36, 36, 36]])


class TestSortMatrixDiagonally(unittest.TestCase):
    def test_sort_diagonally(self):
        mat = [
            [3, 3, 1, 1],
            [2, 2, 1, 2],
            [1, 1, 1, 2]
        ]

        self.assertEqual(sort_matrix_diagonally.sort_diagonally(mat), [
            [1, 1, 1, 1],
            [1, 2, 2, 2],
            [1, 2, 3, 3]
        ])


if __name__ == "__main__":
    unittest.main()
