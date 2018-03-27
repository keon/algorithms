"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections import Iterable

# return list
def flatten(inputArr, outputArr=None):
    if not outputArr:
        outputArr = []
    for ele in inputArr:
        if isinstance(ele, Iterable):
            flatten(ele, outputArr)
        else:
            outputArr.append(ele)
    return outputArr

# returns iterator
def flatten_v2(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten(element)
        else:
            yield element

import unittest

class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [2, 1, 3, 4, 5, 6, 7, 8])
        
    def test_flatten_v2(self):
        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten_v2(nested_list)
        self.assertEqual(next(flattened), 2)
        self.assertEqual(next(flattened), 1)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)


if __name__ == "__main__":
    
    unittest.main()
