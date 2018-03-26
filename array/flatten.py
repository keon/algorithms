from collections import Iterable
from types import GeneratorType

"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.

>>> nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
>>> flattened = flatten(nested_list)
>>> assert next(flattened) == 2
>>> assert next(flattened) == 1
>>> assert next(flattened) == 3
>>> assert next(flattened) == 4
>>> assert next(flattened) == 5
>>> assert next(flattened) == 6
>>> assert next(flattened) == 7
>>> assert next(flattened) == 8
"""


def flatten(iterable: Iterable) -> GeneratorType:
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
    import doctest
    doctest.testmod()