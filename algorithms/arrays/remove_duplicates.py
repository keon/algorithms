"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True, False]
Output: [1, 2, 3, 4, 'hey', 'hello', True, False]
"""


def remove_duplicates(array):
    new_array = []  # Preserve order of first distinct item
    seen = set()  # Track the unique items

    for item in array:
        if all([item is not elem for elem in seen]):
            new_array.append(item)
            seen.add(item)

    return new_array
