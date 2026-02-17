"""Tests for community-contributed algorithms.

Covers algorithms adopted from open PRs and implemented to match
the repo's code standards.
"""

from __future__ import annotations

import unittest

from algorithms.backtracking.minimax import minimax
from algorithms.bit_manipulation.gray_code import gray_code, gray_to_binary
from algorithms.data_structures.kd_tree import KDTree
from algorithms.dynamic_programming.bitmask import tsp
from algorithms.dynamic_programming.count_paths_dp import (
    count_paths_dp,
    count_paths_memo,
    count_paths_recursive,
)
from algorithms.graph.blossom import max_matching
from algorithms.math.linear_regression import linear_regression, r_squared, rmse
from algorithms.math.manhattan_distance import manhattan_distance
from algorithms.math.polynomial_division import polynomial_division
from algorithms.searching.exponential_search import exponential_search
from algorithms.searching.sentinel_search import sentinel_search
from algorithms.string.alphabet_board_path import alphabet_board_path
from algorithms.string.manacher import manacher
from algorithms.string.swap_characters import can_swap_to_equal
from algorithms.string.z_algorithm import compute_z_array, z_search


class TestManacher(unittest.TestCase):
    def test_odd_palindrome(self):
        result = manacher("babad")
        self.assertIn(result, ("bab", "aba"))

    def test_even_palindrome(self):
        self.assertEqual(manacher("cbbd"), "bb")

    def test_single_char(self):
        self.assertEqual(manacher("a"), "a")

    def test_full_palindrome(self):
        self.assertEqual(manacher("racecar"), "racecar")

    def test_empty(self):
        self.assertEqual(manacher(""), "")

    def test_all_same(self):
        self.assertEqual(manacher("aaaa"), "aaaa")


class TestZAlgorithm(unittest.TestCase):
    def test_z_array_basic(self):
        z = compute_z_array("aabxaa")
        self.assertEqual(z[0], 6)
        self.assertEqual(z[1], 1)
        self.assertEqual(z[4], 2)

    def test_z_search_found(self):
        self.assertEqual(z_search("abxabcabcaby", "abcaby"), [6])

    def test_z_search_multiple(self):
        self.assertEqual(z_search("aaaa", "aa"), [0, 1, 2])

    def test_z_search_not_found(self):
        self.assertEqual(z_search("hello", "xyz"), [])

    def test_z_search_empty(self):
        self.assertEqual(z_search("abc", ""), [])
        self.assertEqual(z_search("", "abc"), [])

    def test_z_array_empty(self):
        self.assertEqual(compute_z_array(""), [])


class TestGrayCode(unittest.TestCase):
    def test_2bit(self):
        self.assertEqual(gray_code(2), [0, 1, 3, 2])

    def test_3bit(self):
        self.assertEqual(gray_code(3), [0, 1, 3, 2, 6, 7, 5, 4])

    def test_1bit(self):
        self.assertEqual(gray_code(1), [0, 1])

    def test_0bit(self):
        self.assertEqual(gray_code(0), [0])

    def test_successive_differ_by_one_bit(self):
        codes = gray_code(4)
        for i in range(len(codes) - 1):
            xor = codes[i] ^ codes[i + 1]
            self.assertTrue(xor & (xor - 1) == 0)  # power of 2

    def test_gray_to_binary_roundtrip(self):
        for n in range(16):
            gray = n ^ (n >> 1)
            self.assertEqual(gray_to_binary(gray), n)


class TestKdTree(unittest.TestCase):
    def test_nearest_basic(self):
        points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        tree = KDTree(points)
        self.assertEqual(tree.nearest((9, 2)), (8, 1))

    def test_nearest_exact(self):
        points = [(1, 1), (2, 2), (3, 3)]
        tree = KDTree(points)
        self.assertEqual(tree.nearest((2, 2)), (2, 2))

    def test_nearest_3d(self):
        points = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
        tree = KDTree(points)
        self.assertEqual(tree.nearest((1, 1, 0)), (1, 1, 1))

    def test_single_point(self):
        tree = KDTree([(5, 5)])
        self.assertEqual(tree.nearest((0, 0)), (5, 5))


class TestExponentialSearch(unittest.TestCase):
    def test_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(exponential_search(arr, 7), 3)

    def test_first_element(self):
        self.assertEqual(exponential_search([1, 2, 3], 1), 0)

    def test_last_element(self):
        self.assertEqual(exponential_search([1, 2, 3], 3), 2)

    def test_not_found(self):
        self.assertEqual(exponential_search([1, 2, 3], 4), -1)

    def test_empty(self):
        self.assertEqual(exponential_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(exponential_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(exponential_search([42], 99), -1)


class TestSentinelSearch(unittest.TestCase):
    def test_found(self):
        arr = [4, 2, 7, 1, 9]
        self.assertEqual(sentinel_search(arr, 7), 2)

    def test_last_element(self):
        arr = [4, 2, 7, 1, 9]
        self.assertEqual(sentinel_search(arr, 9), 4)

    def test_not_found(self):
        arr = [4, 2, 7, 1, 9]
        self.assertEqual(sentinel_search(arr, 5), -1)

    def test_empty(self):
        self.assertEqual(sentinel_search([], 1), -1)

    def test_restores_array(self):
        arr = [1, 2, 3]
        sentinel_search(arr, 99)
        self.assertEqual(arr, [1, 2, 3])


class TestManhattanDistance(unittest.TestCase):
    def test_2d(self):
        self.assertEqual(manhattan_distance((1, 2), (4, 6)), 7)

    def test_3d(self):
        self.assertEqual(manhattan_distance((0, 0, 0), (1, 2, 3)), 6)

    def test_same_point(self):
        self.assertEqual(manhattan_distance((3, 4), (3, 4)), 0)

    def test_negative(self):
        self.assertEqual(manhattan_distance((-1, -1), (1, 1)), 4)


class TestLinearRegression(unittest.TestCase):
    def test_basic_fit(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        m, b = linear_regression(x, y)
        self.assertAlmostEqual(m, 0.6)
        self.assertAlmostEqual(b, 2.2)

    def test_perfect_line(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        m, b = linear_regression(x, y)
        self.assertAlmostEqual(m, 2.0)
        self.assertAlmostEqual(b, 0.0)

    def test_r_squared_perfect(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        self.assertAlmostEqual(r_squared(x, y), 1.0)

    def test_rmse_perfect(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        self.assertAlmostEqual(rmse(x, y), 0.0)

    def test_rmse_nonperfect(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 5, 4, 5]
        self.assertGreater(rmse(x, y), 0)

    def test_too_few_points(self):
        with self.assertRaises(ValueError):
            linear_regression([1], [2])


class TestPolynomialDivision(unittest.TestCase):
    def test_basic(self):
        # (x^2 - 3x + 2) / (x - 1) = (x - 2), remainder 0
        q, r = polynomial_division([1, -3, 2], [1, -1])
        self.assertEqual(q, [1.0, -2.0])
        self.assertEqual(r, [0.0])

    def test_with_remainder(self):
        # (x^2 + 1) / (x - 1) = (x + 1), remainder 2
        q, r = polynomial_division([1, 0, 1], [1, -1])
        self.assertAlmostEqual(q[0], 1.0)
        self.assertAlmostEqual(q[1], 1.0)
        self.assertAlmostEqual(r[0], 2.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            polynomial_division([1, 2], [0, 0])


class TestAlphabetBoardPath(unittest.TestCase):
    def test_leet(self):
        path = alphabet_board_path("leet")
        self.assertIn("!", path)
        # Verify length: must spell 4 chars so exactly 4 '!'s
        self.assertEqual(path.count("!"), 4)

    def test_code(self):
        path = alphabet_board_path("code")
        self.assertEqual(path.count("!"), 4)

    def test_z(self):
        # 'z' is at row 5, col 0 — must go down 5 from 'a'
        path = alphabet_board_path("z")
        self.assertEqual(path, "DDDDD!")

    def test_za(self):
        path = alphabet_board_path("za")
        self.assertEqual(path, "DDDDD!UUUUU!")


class TestSwapCharacters(unittest.TestCase):
    def test_can_swap(self):
        self.assertTrue(can_swap_to_equal("ab", "ba"))

    def test_identical(self):
        # No differences — need exactly 2, so False
        self.assertFalse(can_swap_to_equal("ab", "ab"))

    def test_too_many_diffs(self):
        self.assertFalse(can_swap_to_equal("abc", "xyz"))

    def test_different_lengths(self):
        self.assertFalse(can_swap_to_equal("ab", "abc"))

    def test_one_diff(self):
        self.assertFalse(can_swap_to_equal("ab", "ac"))


class TestMinimax(unittest.TestCase):
    def test_depth_2(self):
        # max(min(3,5), min(2,9)) = max(3,2) = 3
        self.assertEqual(minimax(2, True, [3, 5, 2, 9]), 3)

    def test_depth_3(self):
        self.assertEqual(minimax(3, True, [3, 5, 2, 9, 12, 5, 23, 23]), 12)

    def test_single_leaf(self):
        self.assertEqual(minimax(0, True, [42]), 42)

    def test_minimizing(self):
        self.assertEqual(minimax(1, False, [3, 5]), 3)


class TestTsp(unittest.TestCase):
    def test_4_cities(self):
        dist = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0],
        ]
        self.assertEqual(tsp(dist), 80)

    def test_3_cities(self):
        dist = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0],
        ]
        self.assertEqual(tsp(dist), 6)


class TestCountPathsDp(unittest.TestCase):
    def test_3x7(self):
        self.assertEqual(count_paths_dp(3, 7), 28)
        self.assertEqual(count_paths_memo(3, 7), 28)
        self.assertEqual(count_paths_recursive(3, 7), 28)

    def test_3x3(self):
        self.assertEqual(count_paths_dp(3, 3), 6)

    def test_1x1(self):
        self.assertEqual(count_paths_dp(1, 1), 1)

    def test_2x2(self):
        self.assertEqual(count_paths_dp(2, 2), 2)


class TestBlossom(unittest.TestCase):
    def test_path_graph(self):
        # Path: 0-1-2-3 → max matching has 2 edges
        matching = max_matching(4, [(0, 1), (1, 2), (2, 3)])
        self.assertEqual(len(matching), 2)

    def test_triangle(self):
        # Triangle: 0-1-2 → max matching has 1 edge
        matching = max_matching(3, [(0, 1), (1, 2), (0, 2)])
        self.assertEqual(len(matching), 1)

    def test_empty_graph(self):
        matching = max_matching(3, [])
        self.assertEqual(len(matching), 0)

    def test_complete_4(self):
        # K4 → max matching has 2 edges
        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        matching = max_matching(4, edges)
        self.assertEqual(len(matching), 2)


if __name__ == "__main__":
    unittest.main()
