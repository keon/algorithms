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

    Examples:

    >>> interpolation_search([-25, -12, -1, 10, 12, 15, 20, 41, 55], -1)
    2
    >>> interpolation_search([5, 10, 12, 14, 17, 20, 21], 55)
    -1
    >>> interpolation_search([5, 10, 12, 14, 17, 20, 21], -5)
    -1

    """

    # highest and lowest index in array
    high = len(array) - 1
    low = 0

    while (low <= high) and (array[low] <= search_key <= array[high]):
        # calculate the search position
        pos = low + int(((search_key - array[low]) *
                         (high - low) / (array[high] - array[low])))

        # search_key is found 
        if array[pos] == search_key:
            return pos

        # if search_key is larger, search_key is in upper part
        if array[pos] < search_key:
            low = pos + 1
            
        # if search_key is smaller, search_key is in lower part
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
