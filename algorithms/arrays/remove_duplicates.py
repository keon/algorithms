"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]
Output: [1, 2, 3, 4, 'hey', 'hello']

Time Complexity: O(n) for hashable items, O(n²) worst case for unhashable items
Space Complexity: O(n) for the seen set and result array
"""
from collections.abc import Hashable

def remove_duplicates(array):
    seen = set()
    new_array = []

    for item in array:
        if isinstance(item, Hashable):
            if item not in seen:
                seen.add(item)
                new_array.append(item)
        else:
            if item not in new_array:
                new_array.append(item)

    return new_array
