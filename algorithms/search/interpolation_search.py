""" 
Python implementation of the Interpolation Search algorithm.
Given a sorted array in increasing order, interpolation search calculates
the starting point of its search according to the search key.

FORMULA: start_pos = low + [ (x - arr[low])*(high - low) / (arr[high] - arr[low]) ]

Doc: https://en.wikipedia.org/wiki/Interpolation_search

Time Complexity: O(log2(log2 n)) for average cases, O(n) for the worst case.
The algorithm performs best with uniformly distributed arrays.
"""

from typing import List


def interpolation_search(array: List[int], search_key: int) -> int:
    """
    :param array: The array to be searched.
    :param search_key: The key to be searched in the array.

    :returns: Index of search_key in array if found, else -1.

    Example

    >>> interpolation_search([1, 10, 12, 15, 20, 41, 55], 20)
    4
    >>> interpolation_search([5, 10, 12, 14, 17, 20, 21], 55)
    -1

    """

    # highest and lowest index in array
    high = len(array) - 1
    low = 0

    while low <= high and search_key in range(low, array[high] + 1):
        # calculate the search position
        pos = low + int(((search_key - array[low]) *
                         (high - low) / (array[high] - array[low])))

        # if array[pos] equals the search_key then return pos as the index
        if search_key == array[pos]:
            return pos
        # if the search_key is greater than array[pos] restart the search with the
        # subarray greater than array[pos]
        elif search_key > array[pos]:
            low = pos + 1
        # in this case start the search with the subarray smaller than current array[pos]
        elif search_key < array[pos]:
            high = pos - 1

    return -1
