"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable


def flatten(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten(element)
        else:
            yield element


if __name__ == "__main__":
    import unittest

    class TestFlatten(unittest.TestCase):
        def test_flatten(self):
            nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
            flattened = flatten(nested_list)
            self.assertEqual(next(flattened), 2)
            self.assertEqual(next(flattened), 1)
            self.assertEqual(next(flattened), 3)
            self.assertEqual(next(flattened), 4)
            self.assertEqual(next(flattened), 5)
            self.assertEqual(next(flattened), 6)
            self.assertEqual(next(flattened), 7)
            self.assertEqual(next(flattened), 8)

    unittest.main()
