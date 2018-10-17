from algorithms.iterables import (
    convolved_1d, convolved_2d
)

import itertools
import unittest


class TestConvolved1D(unittest.TestCase):
    """Tests copied from:
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/tests/test_convolved_1d.py
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """

    def test_trivial_loop(self):
        expected = tuple(range(7))
        result = []

        for kernel_hover in convolved_1d(expected, kernel_size=1, padding=0, stride=1):
            result.append(*kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_for_with_stride_two(self):
        expected = tuple(range(0, 7, 2))
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=1, padding=0, stride=2):
            result.append(*kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_for_with_padding_one(self):
        expected = tuple([42] + list(range(0, 7)) + [42])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=1, padding=1, stride=1, default_value=42):
            result.append(*kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_two(self):
        expected = tuple([a, b] for a, b in zip(list(range(0, 6)), list(range(1, 7))))
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=2, padding=0, stride=1):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_two_and_stride_two(self):
        expected = ([0, 1], [2, 3], [4, 5], [6, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=2, padding=0, stride=2):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_two_and_stride_two_and_padding_two(self):
        expected = ([None, None], [0, 1], [2, 3], [4, 5], [6, None], [None, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=2, padding=2, stride=2):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_two_and_stride_two_and_padding_three(self):
        expected = ([None, None], [None, 0], [1, 2], [3, 4], [5, 6], [None, None], [None, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=2, padding=3, stride=2):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_three_and_stride_two_and_padding_two(self):
        expected = ([None, None, 0], [0, 1, 2], [2, 3, 4], [4, 5, 6], [6, None, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=3, padding=2, stride=2):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_two_and_stride_three_and_padding_two(self):
        expected = ([None, None], [1, 2], [4, 5], [None, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=2, padding=2, stride=3):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_seven_kernel_of_three_and_stride_three_and_padding_three(self):
        expected = ([None, None, None], [0, 1, 2], [3, 4, 5], [6, None, None], [None, None, None])
        result = []

        for kernel_hover in convolved_1d(list(range(7)), kernel_size=3, padding=3, stride=3):
            result.append(kernel_hover)
        result = tuple(result)

        self.assertEqual(expected, result)


class TestConvolved2D(unittest.TestCase):
    """Tests copied from:
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/tests/test_convolved_1d.py
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """

    def test_trivial_1x1_loop(self):
        base = tuple(tuple(range(i ** 2, 7 + i ** 2)) for i in range(7))
        expected = tuple(([i],) for i in itertools.chain(*base))
        result = []

        for kernel_hover in convolved_2d(base, kernel_size=1, padding=0, stride=1):
            result.append(tuple(kernel_hover))
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_simple_2x2_loop_on_3x2(self):
        base = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        expected = (
            (
                [1, 2],
                [3, 4]
            ), (
                [3, 4],
                [5, 6]
            )
        )
        result = []

        for kernel_hover in convolved_2d(base, kernel_size=2, padding=0, stride=1):
            result.append(tuple(kernel_hover))
        result = tuple(result)

        print(result)
        print(expected)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
